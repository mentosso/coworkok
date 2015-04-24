# coding=utf-8
from __future__ import unicode_literals

from authtools.models import AbstractEmailUser
from django.db import models
from django.utils.functional import cached_property
from accounts.const import *


class User(AbstractEmailUser):
    first_name = models.CharField('First name', max_length=30, blank=True)
    last_name = models.CharField('Last name', max_length=30, blank=True)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=0)

    @cached_property
    def is_company_type(self):
        return self.user_type == USER_TYPE_COMPANY