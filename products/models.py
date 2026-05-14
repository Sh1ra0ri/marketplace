from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name="Название продукта", help_text="Введите название продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", help_text="Введите цену продукта")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение продукта")
    description = models.TextField(blank=True, verbose_name="description", help_text="Введите описание продукта")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
