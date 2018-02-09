from django.contrib.auth.models import User
from django.db import models

from .validators import persona_name_val


class Persona(models.Model):
    name = models.CharField(max_length=64, validators=persona_name_val, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='personae')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'personae'
