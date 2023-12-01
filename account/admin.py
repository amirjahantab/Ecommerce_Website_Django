from django.contrib import admin
from account.models import Account, HomePage

# Register your models here.

class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'telegram_link', 'phone_number', 'email', 'location', 'services',
                'first_title_services', 'second_title_services', 'third_title_services',
                )

    fieldsets = (
        ('General Information', {
            'fields': ('title', 'short_description', 'long_description', 'image')
        }),
        ('Contact Information', {
            'fields': ('telegram_link', 'phone_number', 'email', 'location')
        }),
        ('Services', {
            'fields': (
                'services', 'services_description',
                'first_title_services','first_description_services', 'first_image_services',
                'second_title_services','second_description_services', 'second_image_services',
                'third_title_services', 'third_description_services', 'third_image_services',
                )
        }),
    )

admin.site.register(Account)
admin.site.register(HomePage, HomePageAdmin)
