from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .models import Product, Table, Order, Category, CustomUser
from .serializers import UserSerializer, ProductSerializer, TableSerializer, OrderSerializer
from .serializers import CategorySerializer
from rest_framework import viewsets
from rest_framework import permissions
from .mixins import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCreateView(LoginRequiredMixin, CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProductCreateView(AdminPermissionMixin, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TableCreateView(CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TableListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TableUpdateView(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserDelView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProductDelView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TableDelView(DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OrderDelView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CategoryDelView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





