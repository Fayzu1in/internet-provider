from django.urls import reverse
from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class AllProviders(models.Model):

    name = models.CharField(("Имя"), max_length=100)
    info = models.TextField(("Инфо"), blank=True)

    class Meta:
        verbose_name = ("Провайдер")
        verbose_name_plural = ("Провайдеры")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Providers_detail", kwargs={"pk": self.pk})


class Plan(models.Model):

    provider = models.CharField(("провайдер"), max_length=100)
    name = models.CharField(("линейка"), max_length=100)
    title = models.CharField(("имя"), max_length=100)
    speed = models.CharField(("скорость"), max_length=100)
    price = models.CharField(("прайс"), max_length=100)
    tech = models.CharField(("тех"), max_length=50, default='GPON')
    limit = models.CharField(("лимит"), max_length=100,
                             default='unlim', blank=True)
    day = models.CharField(("день"), max_length=50, default='0')
    night = models.CharField(("ночь"), max_length=50, default='0')
    info = models.TextField(("инфо"), blank=True)
    abonents = models.CharField(("абоненты"), max_length=100, default='physic')
    created = models.DateTimeField(("создан"), auto_now_add=True)

    class Meta:
        verbose_name = ("Тариф")
        verbose_name_plural = ("Тарифы")

    def __str__(self):
        return f'{self.provider}: {self.name} - {self.title}'

    # def get_absolute_url(self):
    #     return reverse("User_detail", kwargs={"pk": self.pk})


class Coverages(models.Model):

    district = models.CharField(("район"), max_length=150)
    street = models.CharField(("улица"), max_length=150)
    # providers = models.TextField(("providers"), max_length=200)
    providers = models.ManyToManyField(
        "data.AllProviders", verbose_name=("провайдеры"))

    class Meta:
        verbose_name = ("Покрытие")
        verbose_name_plural = ("Покрытие")

    def __str__(self):
        return f'{self.district}: {self.street}'

    # def get_absolute_url(self):
    #     return reverse("Coverage_detail", kwargs={"pk": self.pk})


class Callback(models.Model):

    STATUSES = (
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    )

    name = models.CharField(("имя"), max_length=100)
    phone = models.CharField(("номер"), max_length=100)
    city = models.CharField(("город"), max_length=100)
    district = models.CharField(("район"), max_length=100)
    street = models.CharField(("улица"), max_length=100)
    house = models.CharField(("дом"), max_length=100)
    status = models.CharField(
        ("статус"), max_length=100, default='opened', choices=STATUSES)
    plan_id = models.IntegerField(("айди тарифа"))
    created = models.DateTimeField(("создан"), auto_now_add=True)

    class Meta:
        verbose_name = ("Заявка")
        verbose_name_plural = ("Заявки")
        get_latest_by = 'created'

    def __str__(self):
        return f'{self.name}, {self.phone}'

    # def get_absolute_url(self):
    #     return reverse("Callback_detail", kwargs={"pk": self.pk})


class Offer(models.Model):

    name = models.CharField(("название предложения"), max_length=100)
    plans = models.ManyToManyField(
        "data.Plan", verbose_name=("тарифы"), max_length=3)

    class Meta:
        verbose_name = ("Выгодное предложение")
        verbose_name_plural = ("Выгодные предложения")

    def __str__(self):
        return f'{self.name}'

    # def get_absolute_url(self):
    #     return reverse("BestOffer_detail", kwargs={"pk": self.pk})


class TopProviders(models.Model):

    provider = models.ForeignKey("data.AllProviders", verbose_name=(
        "провайдер"), on_delete=models.CASCADE)
    logo = models.ImageField((""), upload_to='images', null=False)

    class Meta:
        verbose_name = ("Топ провайдер")
        verbose_name_plural = ("Топ провайдеры")

    def __str__(self):
        return str(self.provider)

    # def get_absolute_url(self):
    #     return reverse("TopProvider_detail", kwargs={"pk": self.pk})


class BotUsers(models.Model):

    user_id = models.IntegerField(("user-id"))
    username = models.CharField(("username"), max_length=100)
    is_admin = models.BooleanField(("is_admin"), default=False)
    logged = models.DateTimeField(("logged"), auto_now_add=True)

    class Meta:
        verbose_name = ("Пользователь Бота")
        verbose_name_plural = ("Пользователи Бота")

    def __str__(self):
        return self.username
