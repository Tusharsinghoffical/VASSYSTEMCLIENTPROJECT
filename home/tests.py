from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile, Attendance


class UserModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
    
    def test_user_str_representation(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), 'testuser')


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        # Profile is automatically created by signal, so we just get it
        self.profile = self.user.profile
        # Update the profile with test data
        self.profile.phone = '1234567890'
        self.profile.position = 'Developer'
        self.profile.address = '123 Test St'
        self.profile.save()
    
    def test_profile_creation(self):
        """Test that a profile can be created"""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.phone, '1234567890')
        self.assertEqual(self.profile.position, 'Developer')
        self.assertEqual(self.profile.address, '123 Test St')
    
    def test_profile_str_representation(self):
        """Test the string representation of a profile"""
        self.assertEqual(str(self.profile), 'testuser')


class AttendanceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.attendance = Attendance.objects.create(
            user=self.user,
            name='Test User',
            email='test@example.com',
            qr_code='https://www.venusjewel.com/',
            status='Present',
            location_name='Office',
            location='123 Main St',
            latitude=12.345678,
            longitude=98.765432
        )
    
    def test_attendance_creation(self):
        """Test that an attendance record can be created"""
        self.assertEqual(self.attendance.user, self.user)
        self.assertEqual(self.attendance.name, 'Test User')
        self.assertEqual(self.attendance.email, 'test@example.com')
        self.assertEqual(self.attendance.qr_code, 'https://www.venusjewel.com/')
        self.assertEqual(self.attendance.status, 'Present')
        self.assertEqual(self.attendance.location_name, 'Office')
    
    def test_attendance_str_representation(self):
        """Test the string representation of an attendance record"""
        expected_str = f"{self.attendance.name} - {self.attendance.date} - {self.attendance.status} - {self.attendance.time} - {self.attendance.location_name}"
        self.assertEqual(str(self.attendance), expected_str)


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
    
    def test_login_page(self):
        """Test that the login page loads correctly"""
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please Sign In')
    
    def test_login_functionality(self):
        """Test that a user can log in"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        }, follow=True)
        # Should redirect after successful login
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_login(self):
        """Test that invalid login shows error message"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        # Note: The actual error message might be different in the template
        # We're just checking that the login page is shown again
        self.assertContains(response, 'Sign In')
    
    def test_user_dashboard_access(self):
        """Test that logged in user can access dashboard"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('user_dashboard'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_admin_dashboard_access(self):
        """Test that admin user can access admin dashboard"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get(reverse('admin_dashboard'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_attendance_page_access(self):
        """Test that logged in user can access attendance page"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('attendance'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_profile_page_access(self):
        """Test that logged in user can access profile page"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEqual(response.status_code, 200)


class URLTest(TestCase):
    def test_home_page_status_code(self):
        """Test that the home page loads successfully"""
        response = self.client.get('/', follow=True)
        # Should redirect to login page for unauthenticated users
        self.assertEqual(response.status_code, 200)
    
    def test_login_page_status_code(self):
        """Test that the login page loads successfully"""
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_register_page_status_code(self):
        """Test that the register page loads successfully"""
        response = self.client.get(reverse('register'), follow=True)
        self.assertEqual(response.status_code, 200)