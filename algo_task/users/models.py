from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager
)
from django.conf import settings


class User(AbstractUser):
	mobile_number = models.CharField(null=True, max_length=255, unique=True)
	email = models.EmailField(db_index=True, unique=True)
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name