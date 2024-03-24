from django.contrib import admin
from users.models import CustomUser
from orders.admin import OrderAdmin


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('lastname', 'firstname')}
    list_display = ('email', 'firstname', 'lastname', 'is_active', 'is_staff')
    fields = ('user_id', 'email', 'firstname', 'lastname', 'is_active', 'date_joined', 'slug', 'is_staff',
              'is_superuser')
    readonly_fields = ('date_joined', 'user_id')
    search_fields = ('email',)
    inlines = (OrderAdmin,)
