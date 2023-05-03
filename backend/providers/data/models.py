from django.urls import reverse
from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Plan(models.Model):

    # provider = models.CharField(("провайдер"), max_length=100)
    provider = models.ForeignKey("data.AllProviders", verbose_name=(
        "провайдер"), on_delete=models.CASCADE)
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
    is_hot = models.BooleanField(("Выгодный"), default=False)
    router = models.BooleanField(("Есть роутер"))
    created = models.DateTimeField(("создан"), auto_now_add=True)

    class Meta:
        verbose_name = ("Тариф")
        verbose_name_plural = ("Тарифы")

    def __str__(self):
        return f'{self.provider}: {self.name} - {self.title}'

    # def get_absolute_url(self):
    #     return reverse("User_detail", kwargs={"pk": self.pk})


class AllProviders(models.Model):

    name = models.CharField(("Имя"), max_length=100)
    picture = models.ImageField(("Картинка"), upload_to='images/provider')
    info = models.TextField(("Инфо"), blank=True)
    created = models.DateTimeField(("Создан"), auto_now_add=True)
    best_plans = models.ManyToManyField(
        Plan, verbose_name=("Лучшие тарифы"), blank=True)
    is_published = models.BooleanField(("Опубликован"), default=False)

    class Meta:
        verbose_name = ("Провайдер")
        verbose_name_plural = ("Провайдеры")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Providers_detail", kwargs={"pk": self.pk})


class Coverages(models.Model):
    city = models.CharField(("город"), max_length=150)
    district = models.CharField(("район"), max_length=150)
    street = models.CharField(("улица"), max_length=150)
    houses = models.JSONField(("дома"))
    providers = models.ManyToManyField(
        "data.AllProviders", verbose_name=("провайдеры"))
    created = models.DateTimeField(("создан"), auto_now_add=True)
    edited = models.DateTimeField(("изменен"), auto_now=True)
    
    class Meta:
        verbose_name = ("Покрытие")
        verbose_name_plural = ("Покрытие")

    def __str__(self):
        return f'{self.district}: {self.street}: {self.providers}'

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
    plan_id = models.ForeignKey("Plan", verbose_name=(
        "тариф"), on_delete=models.CASCADE)
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
    created = models.DateTimeField(("создан"), auto_now_add=True)

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
    text = models.TextField(("инфо"), blank=True)
    created = models.DateTimeField(("создан"), auto_now_add=True)
    class Meta:
        verbose_name = ("Топ провайдер")
        verbose_name_plural = ("Топ провайдеры")

    def __str__(self):
        return str(self.provider)

    # def get_absolute_url(self):
    #     return reverse("TopProvider_detail", kwargs={"pk": self.pk})


class News(models.Model):

    title = models.CharField(("заголовок"), max_length=150)
    subtitle = models.CharField(("подзаголовок"), max_length=150)
    image1 = models.ImageField(("картинка 1"), upload_to='news', blank=True)
    image2 = models.ImageField(("картинка 2"), upload_to='news', blank=True)
    image3 = models.ImageField(("картинка 3"), upload_to='news', blank=True)
    text1 = models.TextField(("текст 1"))
    text2 = models.TextField(("текст 2"), blank=True)
    published = models.BooleanField(("опубликован"), default=True)
    created = models.DateTimeField(("создан"), auto_now_add=True)
    edited = models.DateTimeField(("изменен"), auto_now=True)

    class Meta:
        verbose_name = ("Новость")
        verbose_name_plural = ("Новости")
        get_latest_by = 'created'
        ordering = ['-created']

    def __str__(self):
        return str(self.title)

    # def get_absolute_url(self):
    #     return reverse("News_detail", kwargs={"pk": self.pk})


class BotUsers(models.Model):

    user_id = models.CharField(("user-id"), max_length=100)
    username = models.CharField(("username"), max_length=100)
    is_admin = models.BooleanField(("is_admin"), default=False)
    logged = models.DateTimeField(("logged"), auto_now_add=True)

    class Meta:
        verbose_name = ("Пользователь Бота")
        verbose_name_plural = ("Пользователи Бота")

    def __str__(self):
        return self.username
