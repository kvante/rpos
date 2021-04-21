from rest_framework import serializers

from .models import *


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CookOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'cooked', 'created_at', 'product',)


class CookOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'cooked',)

class WaiterOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'cooked', 'created_at', 'product',)
