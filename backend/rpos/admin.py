from django.contrib import admin
from .models import CustomUser, Product, Category, Table, Order
#from .custom_user import CustomUser

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Table)
admin.site.register(Order)
#admin.site.register(CustomUser)
