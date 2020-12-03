from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, nickname, password=None):

        if not email:
            raise ValueError("must have user email")
        user = self.model(email=self.normalize_email(email), nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):

        user = self.create_user(
            email=self.normalize_email(email), nickname=nickname, password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
