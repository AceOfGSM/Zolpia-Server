from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, name, password=None):

        if not email:
            raise ValueError("must have user email")
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(
            email=self.normalize_email(email), name=name, password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(email=username)


class User(AbstractUser):
    firstname = None
    last_name = None
    username = None

    objects = UserManager()

    email = models.EmailField(
        _("email address"), unique=True, max_length=128, primary_key=True
    )

    name = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []