from django.urls import reverse
from django.db import models
# from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Plan(models.Model):

    name = models.CharField(("title"), max_length=100)
    title = models.CharField(("name"), max_length=100)
    speed = models.CharField(("speed"), max_length=100)
    price = models.CharField(("price"), max_length=100)

    class Meta:
        verbose_name = ("Plan")
        verbose_name_plural = ("Plans")

    # def __str__(self):
    #     return self.name

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
