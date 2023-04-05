from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .Lesson import Lesson

class Document(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=_("Lesson id"), on_delete=models.CASCADE) 
    docs = models.FileField(_("lesson video"), upload_to='assets/utils/docs', max_length=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
