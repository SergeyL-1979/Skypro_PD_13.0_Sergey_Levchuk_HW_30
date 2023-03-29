from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class User(AbstractUser):
    """Модель пользователя и автора объявлений"""

    STATUS = [
        ("admin", "Администратор"),
        ("moderator", "Модератор"),
        ("member", "Участник"),
    ]

    role = models.CharField(
        _("Права пользователя"), max_length=10, choices=STATUS, default="member"
    )
    age = models.IntegerField(_("Возраст"), null=True, blank=True)
    location = models.ManyToManyField(
        "Location", blank=True, verbose_name="Местоположение"
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return "{} {}".format(self.last_name, (self.username,))


class Location(models.Model):
    """Модель местоположения"""

    name = models.CharField(_("Местоположение"), max_length=50)
    lat = models.DecimalField(_("lat"), max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(_("lng"), max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name
