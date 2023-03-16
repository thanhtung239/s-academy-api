from django.db import models
from .User import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Course (models.Model): 
    users = models.ManyToManyField(User, related_name="courses" ,blank=True, null=True)
    name = models.CharField(_("course name"), max_length=250)
    description = models.CharField(max_length=1000, blank=True)
    logo_path = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)
    learn_times = models.FloatField(blank=True)
    number_lessons = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    delete_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    def __str__(self):
        return self.name
