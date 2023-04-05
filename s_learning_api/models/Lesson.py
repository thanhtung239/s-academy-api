from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from .Course import Course

class Lesson(models.Model):
    title = models.CharField(_("Lesson title"), max_length=255,)
    course = models.ForeignKey(Course, verbose_name=_("Course id"), on_delete=models.CASCADE)
    video_path = models.FileField(_("Video"), upload_to='assets/video/lesson', max_length=255, blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    description = models.CharField(max_length=1000, blank=True)
    learn_time = models.TimeField(_("lesson learn time"), auto_now=False, auto_now_add=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
