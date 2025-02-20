from django.db import models

class Profile(models.Model):
    # Other profile fields...
    cv = models.FileField(upload_to='CV/', null=True, blank=True)

    def __str__(self):
        return "Profile CV"



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
