import uuid
import json
import io
import base64
import qrcode
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    qr_token = models.CharField(max_length=64, unique=True, blank=True, null=True)

    def ensure_qr_token(self):
        if not self.qr_token:
            self.qr_token = uuid.uuid4().hex
            self.save(update_fields=['qr_token'])
        return self.qr_token

    def save(self, *args, **kwargs):
        if not self.qr_token:
            self.qr_token = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def get_qr_payload(self):
        self.ensure_qr_token()
        user = self.user
        return {
            "system": "VAS_ATTENDANCE_SYSTEM",
            "version": "1.0",
            "user_id": user.id,
            "employee_id": f"VJAS-{user.id:04d}",
            "username": user.username,
            "name": user.get_full_name() or user.username,
            "email": user.email or "",
            "phone": self.phone or "",
            "position": self.position or "Employee",
            "qr_token": self.qr_token,
        }

    def get_qr_code_data(self):
        return json.dumps(self.get_qr_payload(), ensure_ascii=False)

    def get_qr_image_bytes(self):
        data = self.get_qr_code_data()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#1e293b", back_color="#ffffff")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        return buffer.getvalue()

    def get_qr_code_base64(self):
        img_bytes = self.get_qr_image_bytes()
        return "data:image/png;base64," + base64.b64encode(img_bytes).decode('utf-8')

    def __str__(self):
        return self.user.username


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    qr_code = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    ATTENDANCE_STATUS = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    )
    status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS, default='Present')
    location_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    check_in = models.TimeField(blank=True, null=True)
    check_out = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} - {self.status} - {self.time} - {self.location_name}"
