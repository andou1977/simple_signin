from django.contrib import admin

from untitled1.models import andouuser


class BookAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password','telephone','image','account')
admin.site.register(andouuser,BookAdmin)