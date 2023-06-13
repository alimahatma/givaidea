# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models

# # Create your models here.

# class CustomerUser(AbstractUser):
#     USER = 'user'
#     ADMIN = 'admin'
#     SUPERADMIN = 'superadmin'
#     ROLE_CHOICES = [
#         (USER, 'User'),
#         (ADMIN, 'Admin'),
#         (SUPERADMIN, 'Superadmin'),
#     ]

#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=USER)
#     gender = models.CharField(max_length=10)
#     phone_number = models.CharField(max_length=20)
#     address = models.CharField(max_length=255)

#     groups = models.ManyToManyField(Group, related_name='costom_users')
#     user_permissions = models.ManyToManyField(Permission, related_name='costom_users')

#     def __str__(self):
#         return self.user