from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Type(models.TextChoices):
        COMOOM = "comum"
        SHOPKEPPER = "lojista"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=Type.choices, default=Type.COMOOM)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"
