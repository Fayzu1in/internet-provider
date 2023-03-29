from django.urls import reverse
from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class AllProviders(models.Model):

    name = models.CharField(("name"), max_length=100)
    info = models.TextField(("info"), blank=True)

    class Meta:
        verbose_name = ("Provider")
        verbose_name_plural = ("Providers")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Providers_detail", kwargs={"pk": self.pk})


class Plan(models.Model):

    provider = models.CharField(("provider"), max_length=100)
    name = models.CharField(("title"), max_length=100)
    title = models.CharField(("name"), max_length=100)
    speed = models.CharField(("speed"), max_length=100)
    price = models.CharField(("price"), max_length=100)
    tech = models.CharField(("tech"), max_length=50, default='GPON')
    limit = models.CharField(("limit"), max_length=100,
                             default='unlim', blank=True)
    day = models.CharField(("day"), max_length=50, default='0')
    night = models.CharField(("night"), max_length=50, default='0')
    info = models.TextField(("info"), blank=True)
    abonents = models.CharField(("abonents"), max_length=100, default='physic')
    created = models.DateTimeField(("created_at"), auto_now_add=True)

    class Meta:
        verbose_name = ("Plan")
        verbose_name_plural = ("Plans")

    def __str__(self):
        return f'{self.provider}: {self.name} - {self.title}'

    # def get_absolute_url(self):
    #     return reverse("User_detail", kwargs={"pk": self.pk})


class Coverages(models.Model):

    district = models.CharField(("district"), max_length=150)
    street = models.CharField(("street"), max_length=150)
    # providers = models.TextField(("providers"), max_length=200)
    providers = models.ManyToManyField(
        "data.AllProviders", verbose_name=("providers"))

    class Meta:
        verbose_name = ("Coverage")
        verbose_name_plural = ("Coverages")

    def __str__(self):
        return f'{self.district}: {self.street}'

    # def get_absolute_url(self):
    #     return reverse("Coverage_detail", kwargs={"pk": self.pk})


class Callback(models.Model):

    STATUSES = (
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    )

    name = models.CharField(("name"), max_length=100)
    phone = models.CharField(("phone"), max_length=100)
    city = models.CharField(("city"), max_length=100)
    district = models.CharField(("district"), max_length=100)
    street = models.CharField(("street"), max_length=100)
    house = models.CharField(("house"), max_length=100)
    status = models.CharField(
        ("status"), max_length=100, default='opened', choices=STATUSES)
    plan_id = models.IntegerField(("plan_id"))
    created = models.DateTimeField(("created_at"), auto_now_add=True)

    class Meta:
        verbose_name = ("Callback")
        verbose_name_plural = ("Callbacks")
        get_latest_by = 'created'

    def __str__(self):
        return f'{self.name}, {self.phone}'

    # def get_absolute_url(self):
    #     return reverse("Callback_detail", kwargs={"pk": self.pk})


class Offer(models.Model):

    name = models.CharField(("offer name"), max_length=100)
    plans = models.ManyToManyField(
        "data.Plan", verbose_name=("Offers"), max_length=3)

    class Meta:
        verbose_name = ("Offer")
        verbose_name_plural = ("Offers")

    def __str__(self):
        return f'{self.name}'

    # def get_absolute_url(self):
    #     return reverse("BestOffer_detail", kwargs={"pk": self.pk})


class TopProviders(models.Model):

    provider = models.ForeignKey("data.AllProviders", verbose_name=(
        "provider"), on_delete=models.CASCADE)
    logo = models.ImageField((""), upload_to='providers/images', null=False)

    class Meta:
        verbose_name = ("TopProviders")
        verbose_name_plural = ("TopProviders")

    def __str__(self):
        return str(self.provider)

    def get_absolute_url(self):
        return reverse("TopProvider_detail", kwargs={"pk": self.pk})


class BotUsers(models.Model):

    user_id = models.IntegerField(("user-id"))
    username = models.CharField(("username"), max_length=100)
    is_admin = models.BooleanField(("is_admin"), default=False)
    logged = models.DateTimeField(("logged"), auto_now_add=True)

    class Meta:
        verbose_name = ("BotUsers")
        verbose_name_plural = ("BotUserss")

    def __str__(self):
        return self.username


