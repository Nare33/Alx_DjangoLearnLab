from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and return a regular user with username, password, date_of_birth, and profile_photo.
        """
        if not username:
            raise ValueError('The username must be set')
        user = self.model(username=username, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and return a superuser with username, password, date_of_birth, and profile_photo.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, date_of_birth, profile_photo, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

