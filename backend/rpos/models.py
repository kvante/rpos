from django.conf import settings
from datetime import datetime

from django.db import models


class Table(models.Model):
    number = models.IntegerField("Номер столика", db_index=True, unique=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    taken = models.BooleanField("Занят", default=False)
    booked = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'


class Category(models.Model):
    name = models.CharField("Категория", max_length=500, db_index=True)
    neatName = models.CharField(max_length=100)
    description = models.TextField("Описание", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    availability = models.IntegerField(default=0, null=True)
    availabilityUpdated = models.DateField(blank=True, null=True)
    ordering = models.IntegerField()
    available = models.BooleanField(blank=True, default=True)

    def _categoryNeatName(self):
        return self.category.neatName

    categoryNeatName = property(_categoryNeatName)

    def _categoryId(self):
        return self.category.id

    categoryId = property(_categoryId)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    notes = models.CharField(max_length=500, blank=True, null=True)

    started = models.DateTimeField(auto_now=True)
    closed = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()

    reported = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)

    comment = models.CharField(max_length=500, blank=True, null=True)
    cooked = models.BooleanField(default=False)
    reduced = models.PositiveIntegerField(default=0)

    openedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='openedBy', on_delete=models.CASCADE)
    closedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='closedBy', blank=True, null=True,
                                 on_delete=models.CASCADE)
    operatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='operatedBy', on_delete=models.CASCADE)

    def _tableId(self):
        return self.table.id

    tableId = property(_tableId)

    def __unicode__(self):
        return self.table.nickname + " / " + datetime.strftime(self.started, "%Y-%m-%d %H:%M")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
