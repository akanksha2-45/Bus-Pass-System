from django.contrib import admin
from home.models import Contact
from home.models import Buyticket
from home.models import Buypass

# Register your models here.
admin.site.register(Contact)
admin.site.register(Buyticket)
admin.site.register(Buypass)