from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.
class SaveBookData(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    bookname=models.CharField(max_length=300)
    auther_name=models.CharField(max_length=300)
    total_book=models.IntegerField()



#**************************************************************
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)


class MyUserManager(BaseUserManager):
    def create_user(self, email,studentname,classname,branch,mobile_no, date_of_birth,address, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            studentname=studentname,
            classname=classname,
            branch =branch,
            mobile_no=mobile_no,
            date_of_birth=date_of_birth,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,studentname,classname,branch,mobile_no, date_of_birth, address,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            studentname=studentname,
            classname=classname,
            branch=branch,
            mobile_no=mobile_no,
            date_of_birth=date_of_birth,
            address=address
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MycustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    studentname = models.CharField(max_length=120)
    classname = models.CharField(max_length=120)
    branch = models.CharField(max_length=120)
    mobile_no = models.IntegerField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['studentname','classname','branch','mobile_no','date_of_birth','address']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

 
class Bookissue(models.Model):
    email = models.EmailField(verbose_name='email address',max_length=255)
    bookname=models.CharField(max_length=300)
    auther_name=models.CharField(max_length=300)
    total_book=models.IntegerField()
    date = models.DateField()