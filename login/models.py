# import uuid

# from django.db import models
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils import timezone



# # Create your models here.
# class User(AbstractBaseUser, PermissionsMixin):
  
#    # These fields tie to the roles!
#     ADMIN = 1
#     MANAGER = 2
#     EMPLOYEE = 3

#     ROLE_CHOICES = (
#         (ADMIN, 'Admin'),
#         (MANAGER, 'Production'),
#         (EMPLOYEE, 'Breakdown')
#     )
    
#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'

#     # Roles created here
#     uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
#     username = models.CharField(unique=True, max_length=30)
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=1)
#     date_joined = models.DateTimeField(auto_now_add=True)


#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     # objects = CustomUserManager()

#     def __str__(self):
#         return self.username