from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import date, timedelta, timezone
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
import time


# Create your models here.
class BaseModel(models.Model):
    """
    Base Model with created_at, and modified_at fields, will be inherited
    in all other models.
    """

    meta_created_ts = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name=_("Meta Created TimeStamp"),
        null=True,
        blank=True,
    )
    meta_updated_ts = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name=_("Meta Updated TimeStamp"),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

# Image path for profile
def profile_image_path(instance, filename):
    filebase, extension = filename.split(".")
    return "profile_images/%s.%s" % (
        str(int(round(time.time() * 1000))),
        extension,
    )

# ================================= #
# 1 User Table
class User(AbstractUser, BaseModel):
    
    class DietType(models.IntegerChoices):
        VEGETARIAN = 1
        NON_VEGETARIAN = 2
        EGGITARIAN = 3
    
    email = models.CharField(max_length=100, null=True, blank=True, unique=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    goal = models.CharField(max_length=500, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    existing_gym = models.CharField(max_length=100, blank=True, null=True)
    diet_type = models.IntegerField(blank=True, null=True, choices=DietType.choices, default=DietType.VEGETARIAN)
    profile_picture = models.ImageField(max_length=200, upload_to=profile_image_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateField(default=date.today)
    modified_date = models.DateField(default=date.today)
    is_send_email = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    # history = HistoricalRecords()

    class Meta:
        verbose_name_plural = ("Users")
        db_table = "user"

    def __str__(self):
        return self.email

    def tokens(self):
        token = Token.objects.get_or_create(user=self)[0].key
        return {"token": token}

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]