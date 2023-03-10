from django.urls import reverse
from django.db import models
# from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Plan(models.Model):

    provider = models.CharField(("provider"), max_length=100)
    name = models.CharField(("title"), max_length=100)
    title = models.CharField(("name"), max_length=100)
    speed = models.CharField(("speed"), max_length=100)
    price = models.CharField(("price"), max_length=100)

    class Meta:
        verbose_name = ("Plan")
        verbose_name_plural = ("Plans")

    def __str__(self):
        return f'{self.provider}: {self.title}'

    # def get_absolute_url(self):
    #     return reverse("User_detail", kwargs={"pk": self.pk})


class Coverage(models.Model):

    district = models.CharField(("district"), max_length=150)
    street = models.CharField(("street"), max_length=150)
    houses = models.TextField(("houses"), max_length=1000)

    class Meta:
        verbose_name = ("Coverage")
        verbose_name_plural = ("Coverages")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Coverage_detail", kwargs={"pk": self.pk})


class Callback(models.Model):

    name = models.CharField(("name"), max_length=100)
    phone = models.CharField(("phone"), max_length=100)
    email = models.EmailField(("email"), max_length=254, blank=True)
    city = models.CharField(("city"), max_length=100)
    district = models.CharField(("district"), max_length=100)
    street = models.CharField(("street"), max_length=100)
    house = models.CharField(("house"), max_length=100)


    class Meta:
        verbose_name = ("Callback")
        verbose_name_plural = ("Callbacks")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Callback_detail", kwargs={"pk": self.pk})


class Offer(models.Model):
    
    name = models.CharField(("offer name"), max_length=100)
    plans = models.ManyToManyField("data.Plan", verbose_name=("Offers"))

    class Meta:
        verbose_name = ("Offer")
        verbose_name_plural = ("Offers")

    def __str__(self):
        return f'{self.name}'

    # def get_absolute_url(self):
    #     return reverse("BestOffer_detail", kwargs={"pk": self.pk})



class TopProvider(models.Model):

    name = models.CharField(("name"), max_length=100)
    logo = models.ImageField((""), upload_to='providers/images', null=False)
    

    class Meta:
        verbose_name = ("TopProvider")
        verbose_name_plural = ("TopProviders")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("TopProvider_detail", kwargs={"pk": self.pk})
