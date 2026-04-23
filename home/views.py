import csv
import json
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.utils.timezone import localtime, now
from django.db.models import Q, Count
from django.db.models.functions import TruncWeek, TruncMonth, TruncYear
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.sessions.models import Session
from .models import Attendance, Profile
from .forms import UserForm, ProfileForm, AdminUserCreationForm, CustomUserCreationForm


def is_admin(user):
    return user.is_staff or user.is_superuser


@login_required
def redirect_after_login(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('admin_dashboard')
    return redirect('user_dashboard')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('redirect_after_login')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('redirect_after_login')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required
def admin_dashboard(request):
    today = timezone.now().date()
    # Total users present today (Checked in but not checked out yet)
    live_present_count = Attendance.objects.filter(
        date=today, check_out__isnull=True).exclude(check_in__isnull=True).count()
    total_users = User.objects.count()
    active_sessions = Session.objects.filter(
        expire_date__gte=timezone.now()).count()

    # Get recent attendance records (last 10)
    recent_attendance = Attendance.objects.select_related(
        'user').order_by('-date', '-check_in')[:10]

    return render(request, 'admin_dashboard.html', {
        'total_users': total_users,
        'live_present_count': live_present_count,
        'active_sessions': active_sessions,
        'recent_attendance': recent_attendance,
    })


@staff_member_required
def live_present_count_api(request):
    today = timezone.now().date()
    count = Attendance.objects.filter(
        date=today, check_out__isnull=True).exclude(check_in__isnull=True).count()
    return JsonResponse({'live_present_count': count})


@login_required
def user_dashboard(request):
    attendance_records = Attendance.objects.filter(
        user=request.user).order_by('-date', '-check_in')[:5]
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'user_dashboard.html', {
        'user': request.user,
        'profile': profile,
        'attendance_records': attendance_records,
    })


@login_required
def attendance(request):
    user = request.user
    base_template = 'admin_base.html' if user.is_staff or user.is_superuser else 'index.html'
    return render(request, 'attendance.html', {
        "user": user,
        "name": user.get_full_name() or user.username,
        "email": user.email,
        "username": user.username,
        "user_id": user.id,
        "base_template": base_template,
    })


@login_required
def attendance_history(request):
    records = Attendance.objects.filter(
        user=request.user).order_by('-date', '-check_in')
    return render(request, 'attendance_history.html', {
        'records': records,
        'name': request.user.get_full_name() or request.user.username,
    })


@login_required
def mark_attendance(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            qr_data = data.get("qr_data")
            location_name = data.get("location_name")
            mode = data.get("mode", "check_in")
            today = timezone.now().date()
            now_time = localtime().time()

            if qr_data != settings.ALLOWED_QR_CODE:
                return JsonResponse({"error": "❌ Invalid QR Code scanned."}, status=403)

            record, created = Attendance.objects.get_or_create(
                user=request.user,
                date=today,
                defaults={
                    "name": request.user.get_full_name() or request.user.username,
                    "email": request.user.email,
                    "qr_code": qr_data,
                    "location_name": location_name,
                }
            )

            if mode == "check_in":
                if record.check_in:
                    return JsonResponse({"message": "ℹ️ Already Checked In today."})
                record.check_in = now_time
                record.save()
                return JsonResponse({"message": "✅ Check-In marked successfully!"})

            elif mode == "check_out":
                if not record.check_in:
                    return JsonResponse({"message": "⚠️ You need to Check-In first."})
                if record.check_out:
                    return JsonResponse({"message": "ℹ️ Already Checked Out today."})
                record.check_out = now_time
                record.save()
                return JsonResponse({"message": "✅ Check-Out marked successfully!"})
            return JsonResponse({"error": "❌ Invalid mode."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


@staff_member_required
def attendance_report_view(request):
    today = timezone.now().date()
    attendance_records = Attendance.objects.select_related(
        'user').all().order_by('-date', '-check_in')

    # Populate name and email from user if not set
    for record in attendance_records:
        if not record.name:
            record.name = record.user.get_full_name() or record.user.username
        if not record.email:
            record.email = record.user.email

    import datetime
    for record in attendance_records:
        if record.check_in and record.check_out:
            dt1 = datetime.datetime.combine(
                datetime.date.today(), record.check_in)
            dt2 = datetime.datetime.combine(
                datetime.date.today(), record.check_out)
            if dt2 < dt1:
                dt2 += datetime.timedelta(days=1)
            diff = dt2 - dt1
            total_seconds = diff.total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            record.working_hours_str = f"{hours}h {minutes}m"
            record.working_hours = round(total_seconds / 3600, 2)
        else:
            record.working_hours_str = "--"
            record.working_hours = 0

    present_today = attendance_records.filter(date=today).count()
    active_now = attendance_records.filter(
        date=today, check_out__isnull=True).exclude(check_in__isnull=True).count()
    total_users = User.objects.count()

    # Chart Data: Last 15 completed shifts spanning across users
    completed_records = [
        r for r in attendance_records if r.working_hours > 0][:15]
    completed_records.reverse()
    chart_labels = [
        f"{r.name or r.user.username} ({r.date.strftime('%b %d')})" for r in completed_records]
    chart_data = [r.working_hours for r in completed_records]

    return render(request, 'attendance_report.html', {
        'records': attendance_records[:200],  # Last 200 activity logs
        'present_today': present_today,
        'active_now': active_now,
        'total_users': total_users,
        'chart_labels': json.dumps(chart_labels),
        'chart_data': json.dumps(chart_data),
    })


@staff_member_required
def manage_users_view(request):
    query = request.GET.get('q', '')
    users = User.objects.all().order_by('-date_joined')
    if query:
        users = users.filter(Q(username__icontains=query)
                             | Q(email__icontains=query))
    paginator = Paginator(users, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'manage_users.html', {'users': page_obj, 'query': query})


@staff_member_required
def edit_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        profile.phone = request.POST.get('phone')
        profile.position = request.POST.get('position')
        profile.address = request.POST.get('address')
        user.save()
        profile.save()
        messages.success(request, "✅ User updated successfully!")
        return redirect('manage_users')
    return render(request, 'edit_user.html', {'user': user, 'profile': profile})


@staff_member_required
def delete_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "🗑️ User deleted successfully!")
    return redirect('manage_users')


@staff_member_required
def register_admin(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Admin account created!')
            return redirect('manage_users')
    else:
        form = AdminUserCreationForm()
    return render(request, 'register.html', {'form': form, 'title': 'Register Admin', 'show_back_link': True})


@staff_member_required
def add_user_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ New employee added!")
            return redirect('manage_users')
    else:
        form = CustomUserCreationForm()
    return render(request, 'add_user.html', {'form': form})


@staff_member_required
def reports_view(request):
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    staff_users = User.objects.filter(is_staff=True).count()
    recent_logins = User.objects.exclude(
        last_login=None).order_by('-last_login')[:10]
    return render(request, 'reports.html', {
        'total_users': total_users,
        'active_users': active_users,
        'staff_users': staff_users,
        'recent_logins': recent_logins,
    })


@staff_member_required
def user_attendance_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    records = Attendance.objects.filter(
        user=user).order_by('-date', '-check_in')
    return render(request, 'user_attendance_detail.html', {'user_obj': user, 'records': records})


@staff_member_required
def download_users_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'Is Staff', 'Date Joined'])
    for u in User.objects.all():
        writer.writerow([u.username, u.email, u.is_staff, u.date_joined])
    return response


@login_required
def profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "✅ Profile updated!")
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form, 'profile': profile, 'user': user})


@staff_member_required
def user_detail_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})


@staff_member_required
def download_user_csv(request, user_id):
    user = get_object_or_404(User, id=user_id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="user_{user.username}.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Username', 'Email', 'First Name',
                    'Last Name', 'Date Joined'])
    writer.writerow([user.id, user.username, user.email,
                    user.first_name, user.last_name, user.date_joined])
    return response


@staff_member_required
def download_csv(request):
    # Default for download_csv button on dashboard
    return download_users_csv_view(request)


def register(request):
    if request.user.is_authenticated:
        return redirect('redirect_after_login')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "✅ Account created successfully!")
            return redirect('redirect_after_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {
        'form': form,
        'title': 'Employee Registration',
        'button_text': 'Create Account',
        'show_login_link': True
    })


@staff_member_required
def export_attendance_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'
    writer = csv.writer(response)
    writer.writerow(['User', 'Date', 'Check-In', 'Check-Out', 'Location'])
    for record in Attendance.objects.all().order_by('-date'):
        writer.writerow([record.user.username, record.date,
                        record.check_in, record.check_out, record.location_name])
    return response
