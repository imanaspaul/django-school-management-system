from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        """
        Creates and saves a superuser with the given email, full_name and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name=full_name

        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    def create_teacher(self, email, full_name, password):
        """
        Creates and saves a superuser with the given email, full_name and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name=full_name

        )
        user.is_teacher = True
        user.save(using=self._db)
        return user
    
    def create_student(self, email, full_name, password):
        '''
        Creating Teacher with full name and email 
        '''
        user = self.creat_user(
            email,
            password=password,
            full_name=full_name
        )
        user.is_student = True
        user.save(using=self.db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_student = models.BooleanField(default=False, verbose_name='Student')
    is_teacher = models.BooleanField(default=False, verbose_name="Teacher")

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

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
        
