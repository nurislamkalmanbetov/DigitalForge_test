from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email адрес', unique=True, db_index=True)
    phone = models.CharField('Номер телефона', max_length=50, blank=True, db_index=True)
    is_staff = models.BooleanField('Сотрудник', default=False)
    is_manager = models.BooleanField('Менеджер отдела продаж', default=False)
    is_superuser = models.BooleanField('Суперпользователь', default=False)
    is_active = models.BooleanField('Активен', default=False)
    is_delete = models.BooleanField('Удален', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




class SalesManager(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    deals_count = models.PositiveIntegerField(default=0, verbose_name='Количество сделок')
    temporary_password = models.CharField(max_length=50, verbose_name='Временный пароль')

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'



class HousingObject(models.Model):
    STATUS_CHOICES = [
        ('Economy', 'Эконом'),
        ('Comfort', 'Комфорт'),
        ('Business', 'Бизнес'),
        ('Premium', 'Премиум'),
    ]
    
    title = models.CharField(max_length=100, verbose_name='Название дома объекта')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус объекта')
    floors = models.IntegerField(verbose_name='Этажность')
    apartments_count = models.IntegerField(verbose_name='Количество квартир')
    entrances_count = models.IntegerField(verbose_name='Количество подъездов')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект ЖК'
        verbose_name_plural = 'Объекты ЖК'



class Apartment(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Активная'),
        ('Booked', 'Бронь'),
        ('Sold', 'Куплено'),
        ('Barter', 'Бартер'),
        ('Installment', 'Рассрочка'),
        ('Cancelled', 'Отмена'),
    ]

    APARTMENT_TYPES = [
        ('1-room 45sqm', '1-комнатная (45 кв.м)'),
        ('1-room Studio 55sqm', '1-комнатная студия (55 кв.м)'),
        ('2-room 65sqm', '2-комнатная (65 кв.м)'),
        ('2-room Studio 75sqm', '2-комнатная студия (75 кв.м)'),
        ('3-room 85sqm', '3-комнатная (85 кв.м)'),
        ('4-room 144sqm', '4-комнатная (144 кв.м)'),
        ('Penthouse', 'Пентхаус'),
    ]
    
    number = models.CharField(max_length=50, verbose_name='Номер квартиры')
    housing_object = models.ForeignKey(HousingObject, on_delete=models.CASCADE, verbose_name='Объект')
    floor = models.IntegerField(verbose_name='Этаж')
    type = models.CharField(max_length=50, choices=APARTMENT_TYPES, verbose_name='Тип квартиры')
    booking_date = models.DateField(null=True, blank=True, verbose_name='Дата брони')
    booking_status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name='Статус брони')
    price = models.CharField(max_length=100, verbose_name='Цена')
    client = models.CharField(max_length=100, blank=True, null=True, verbose_name='Клиент')
    phone_number_customer = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона клиента')
    number_contract = models.CharField(max_length=50, blank=True, null=True, verbose_name='Номер контракта')
    sales_manager = models.ForeignKey(SalesManager, on_delete=models.SET_NULL, null=True, verbose_name='Менеджер продаж')


    def get_booking_status_display(self):
        if self.booking_status == 'Sold':
            return f'Куплено {self.booking_date}'
        elif self.booking_status == 'Booked':
            return f'Бронь до {self.booking_date}'
        else:
            return ''

    def __str__(self):
        return f'{self.number}, {self.housing_object.title}'
    
    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
