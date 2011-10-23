from django.contrib import admin
from store.models import Beer 
from store.models import BeverageStyle
from store.models import Company

admin.site.register(Beer)
admin.site.register(BeverageStyle)
admin.site.register(Company)

