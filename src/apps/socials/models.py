from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class SocialAccountBase(models.Model):
    username = models.TextField(unique=True)
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    class Meta:
        abstract = True


class SocialAccountDiscord(SocialAccountBase):
    pass


class SocialAccountX(SocialAccountBase):
    pass


class SocialAccountTelegram(SocialAccountBase):
    pass


class SocialAccountTelegramCode(models.Model):
    username = models.TextField(unique=True)
    uuid = models.UUIDField()
    datetime_created = models.DateTimeField(auto_now_add=True)


class SocialAccountGithub(SocialAccountBase):
    pass