from django.contrib import admin
from .models import User, SalesManager, HousingObject, Apartment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'is_staff', 'is_manager', 'is_superuser', 'is_active', 'is_delete')
    search_fields = ('email', 'phone')
    list_filter = ('is_staff', 'is_manager', 'is_superuser', 'is_active', 'is_delete')
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_manager', 'is_superuser', 'is_active', 'is_delete')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2', 'is_staff', 'is_manager', 'is_superuser', 'is_active', 'is_delete')}
        ),
    )
    ordering = ('email',)


@admin.register(SalesManager)
class SalesManagerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'created_date', 'deals_count')
    search_fields = ('full_name', 'phone', 'email')
    list_filter = ('created_date',)
    ordering = ('-created_date',)


@admin.register(HousingObject)
class HousingObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'floors', 'apartments_count', 'entrances_count', 'address')
    search_fields = ('title', 'address')
    list_filter = ('status',)
    ordering = ('title',)


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number', 'housing_object', 'floor', 'type', 'booking_date', 'booking_status', 'price', 'client', 'phone_number_customer', 'number_contract', 'sales_manager')
    search_fields = ('number', 'housing_object__title', 'client', 'phone_number_customer', 'number_contract')
    list_filter = ('booking_status',)
    ordering = ('number',)
