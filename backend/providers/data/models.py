from django.urls import reverse
from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import pre_save, post_init
from django.dispatch import receiver
import html
import re
# Create your models here.


class Plan(models.Model):

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
    daily_speed_time = models.CharField(
        'Скорость днем (Со сколько до скольки)', max_length=50, default='08:00-00:00')
    night = models.CharField(("ночь"), max_length=50, default='0')
    nightly_speed_time = models.CharField(
        'Скорость ночью (Со сколько до скольки)', max_length=50, default='00:00-08:00')
    tasix = models.CharField(("тасикс"), max_length=50, default='0')
    info = models.TextField(("инфо"), blank=True)
    abonents = models.CharField(("абоненты"), max_length=100, default='physic')
    is_hot = models.BooleanField(("Выгодный"), default=False)
    router = models.BooleanField(("Есть роутер"), default=False)
    router_text = models.TextField(("Инфо о роутере"), blank=True)
    tv = models.BooleanField(("Есть ТВ"), default=False)
    tv_text = models.TextField(("Инфо о ТВ"), blank=True)
    cabel = models.BooleanField(("Есть кабель"), default=False)
    cabel_text = models.TextField(("Инфо о кабеле"), blank=True)
    more_info = models.TextField(("Доп инфо"), blank=True)
    created = models.DateTimeField(("создан"), auto_now_add=True)

    class Meta:
        verbose_name = ("Тариф")
        verbose_name_plural = ("Тарифы")
        ordering = ['-provider__position', '-created']

    def __str__(self):
        return f'{self.provider}: {self.name} - {self.title}'

    # def get_absolute_url(self):
    #     return reverse("User_detail", kwargs={"pk": self.pk})


@receiver(pre_save, sender=Plan)
def replace_tabs_and_spaces(sender, instance, **kwargs):
    # instance.info = html.escape(instance.info).replace('\t', '&#9;').replace(' ', '&#32;')
    # instance.router_text = html.escape(instance.router_text).replace('\t', '&#9;').replace(' ', '&#32;')
    # instance.cabel_text = html.escape(instance.cabel_text).replace('\t', '&#9;').replace(' ', '&#32;')
    # instance.tv_text = html.escape(instance.tv_text).replace('\t', '&#9;').replace(' ', '&#32;')
    # instance.more_info = html.escape(instance.more_info).replace('\t', '&#9;').replace(' ', '&#32;')
    instance.info = re.sub(r'(?<!")([\t ])', lambda m: '&#9;' if m.group(
        1) == '\t' else '&#32;', instance.info)
    instance.router_text = re.sub(r'(?<!")([\t ])', lambda m: '&#9;' if m.group(
        1) == '\t' else '&#32;', instance.router_text)
    instance.cabel_text = re.sub(r'(?<!")([\t ])', lambda m: '&#9;' if m.group(
        1) == '\t' else '&#32;', instance.cabel_text)
    instance.tv_text = re.sub(r'(?<!")([\t ])', lambda m: '&#9;' if m.group(
        1) == '\t' else '&#32;', instance.tv_text)
    instance.more_info = re.sub(r'(?<!")([\t ])', lambda m: '&#9;' if m.group(
        1) == '\t' else '&#32;', instance.more_info)


@receiver(post_init, sender=Plan)
def replace_html_entities(sender, instance, **kwargs):
    # instance.info = instance.info.replace('&#9;', '\t').replace('&#32;', ' ')
    # instance.router_text = instance.router_text.replace('&#9;', '\t').replace('&#32;', ' ')
    # instance.cabel_text = instance.cabel_text.replace('&#9;', '\t').replace('&#32;', ' ')
    # instance.tv_text = instance.tv_text.replace('&#9;', '\t').replace('&#32;', ' ')
    # instance.more_info = instance.more_info.replace('&#9;', '\t').replace('&#32;', ' ')
    instance.info = instance.info.replace('&#9;', '\t').replace('&#32;', ' ')
    instance.router_text = instance.router_text.replace(
        '&#9;', '\t').replace('&#32;', ' ')
    instance.cabel_text = instance.cabel_text.replace(
        '&#9;', '\t').replace('&#32;', ' ')
    instance.tv_text = instance.tv_text.replace(
        '&#9;', '\t').replace('&#32;', ' ')
    instance.more_info = instance.more_info.replace(
        '&#9;', '\t').replace('&#32;', ' ')


class AllProviders(models.Model):


    name = models.CharField(("Имя"), max_length=100)
    picture = models.ImageField(("Картинка"), upload_to='images/provider')
    info = models.TextField(("Инфо"), blank=True)
    created = models.DateTimeField(("Создан"), auto_now_add=True)
    best_plans = models.ManyToManyField(
        Plan, verbose_name=("Лучшие тарифы"), blank=True)
    is_published = models.BooleanField(("Опубликован"), default=False)
    position = models.PositiveIntegerField(("position"), default=0)
    class Meta:
        verbose_name = ("Провайдер")
        verbose_name_plural = ("Провайдеры")
        ordering = ['-position', '-created']

    def __str__(self):
        return self.name


@receiver(pre_save, sender=AllProviders)
def replace_tabs_and_spaces(sender, instance, **kwargs):
    instance.info = html.escape(instance.info).replace(
        '\t', '&#9;').replace(' ', '&#32;')


@receiver(post_init, sender=AllProviders)
def replace_html_entities(sender, instance, **kwargs):
    instance.info = instance.info.replace('&#9;', '\t').replace('&#32;', ' ')

    # def get_absolute_url(self):
    #     return reverse("Providers_detail", kwargs={"pk": self.pk})


class Coverages(models.Model):
    city = models.CharField(("город"), max_length=150)
    district = models.CharField(("район"), max_length=150)
    street = models.CharField(("улица"), max_length=150)
    houses = models.TextField(("дома"),  blank=True, default='')
    providers = models.ManyToManyField(
        "data.AllProviders", verbose_name=("провайдеры"), blank=True)
    created = models.DateTimeField(("создан"), auto_now_add=True)
    edited = models.DateTimeField(("изменен"), auto_now=True)
    freelink_houses = models.TextField(
        ("дома с фрилинком"), blank=True, default='')
    comnet_houses = models.TextField(
        ("дома с комнетом"), blank=True, default='')
    sarkor_houses = models.TextField(
        ("дома с саркором"), blank=True, default='')
    ars_inform_houses = models.TextField(
        ("дома с арс инфор"), blank=True, default='')
    uzonline_houses = models.TextField(
        ("дома с узонлайном"), blank=True, default='')
    city_net_houses = models.TextField(
        ("дома с ситинетом"), blank=True, default='')
    gals_houses = models.TextField(("дома с галс"), blank=True, default='')
    spectr_houses = models.TextField(("дома с спектр"), blank=True, default='')
    optikom_houses = models.TextField(
        ("дома с оптиком"), blank=True, default='')
    sirius_houses = models.TextField(("дома с сириус"), blank=True, default='')

    class Meta:
        verbose_name = ("Покрытие")
        verbose_name_plural = ("Покрытие")
        ordering = ['district', 'street']

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
        ordering = ['-provider__position', '-created']

    def __str__(self):
        return str(self.provider)
    
    

@receiver(pre_save, sender=TopProviders)
def replace_tabs_and_spaces(sender, instance, **kwargs):
    instance.text = html.escape(instance.text).replace(
        '\t', '&#9;').replace(' ', '&#32;')


@receiver(post_init, sender=TopProviders)
def replace_html_entities(sender, instance, **kwargs):
    instance.text = instance.text.replace('&#9;', '\t').replace('&#32;', ' ')


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


class Adressless(models.Model):
    status_choices = (
        ('opened', 'Opened'),
        ('closed', 'Closed'),
    )
    phone = models.CharField(("номер"), max_length=100)
    status = models.CharField(
        ("статус"), max_length=100, choices=status_choices, default='opened')
    created = models.DateTimeField(("создан"), auto_now_add=True)

    class Meta:
        verbose_name = ("Заявка без адреса")
        verbose_name_plural = ("Заявки без адреса")
        # get_latest_by = 'created'
        ordering = ['created']

    def __str__(self):
        return f'{self.phone}: {self.status}'


class QuestionAndAnswers(models.Model):
    question = models.CharField(("Вопрос"), max_length=255)
    answer = models.TextField("Ответ")
    created = models.DateTimeField(("Создвн"), auto_now_add=True)
    updated = models.DateTimeField(("Изменен"), auto_now=True)

    class Meta:
        verbose_name = "Вопрос и ответ"
        verbose_name_plural = "Вопросы и ответы"
        ordering = ['created']

    def __str__(self):
        return f'{self.question}'


class QuickCallback(models.Model):

    name = models.CharField(("Имя"), max_length=100)
    phone = models.CharField(("Номер телефона"), max_length=10)
    preferrable_time = models.CharField(
        ("Когда удобно говорить"), max_length=100)
    created = models.DateTimeField(("Создвн"), auto_now_add=True)
    updated = models.DateTimeField(("Изменен"), auto_now=True)

    class Meta:
        verbose_name = ("Заявка на обратный звонок")
        verbose_name_plural = ("Заявки на обратный звонок (С главной)")



class ClickEvent(models.Model):
    ip = models.CharField(max_length=50, verbose_name='ip adress', blank=True, default='0.0.0.0')
    title = models.CharField(("title"), max_length=100, blank=True)
    device = models.CharField(max_length=255, verbose_name='device', blank=True, default='none')
    click_time = models.DateTimeField(auto_now_add=True, verbose_name='click time')


    class Meta:
        verbose_name = "Клик (статистика)"
        verbose_name_plural = "Клики (статистика)"
