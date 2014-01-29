from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('customer', 'Customer'),
        ('qa_enginer', 'Qa enginer'),
        ('reporter', 'Reporter')
    )

    role = models.SlugField(default='developer', choices=ROLES)


