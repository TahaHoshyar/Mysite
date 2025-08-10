from django.contrib import admin
from website.models import Contact , Newsletter

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['name' , 'message']
    list_filter = ('email',)


# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)