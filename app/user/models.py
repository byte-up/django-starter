from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from core.models import Base

class User(AbstractUser):
    is_verified = models.BooleanField(_('Verified'), default=False, blank=True)

    class Meta:
        verbose_name = _('Users')
        verbose_name_plural = _('Users')


class Notification(Base):
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
