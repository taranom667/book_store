from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class AllObjectsUserManager(CustomManager):
    def get_queryset(self):
        return super().get_queryset()


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(null=True,blank=True,max_length=11, unique=True)
    national_code = models.CharField(max_length=11, unique=True, null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)

    objects = CustomManager()
    all_objects = AllObjectsUserManager()

    def __str__(self):
        return str(self.id) + "  " + self.username


class Author(User):
    name = models.CharField(max_length=100, unique=True, default="unknown")
    nickname = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    all_objects = AllObjectsUserManager()

    def __str__(self):
            return str(self.id)+ "  "+self.username

