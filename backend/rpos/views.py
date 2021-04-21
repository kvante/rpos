from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Table, Order, Category
from .serializers import ProductSerializer, TableSerializer, OrderSerializer, CookOrderSerializer
from .serializers import CookOrderUpdateSerializer
from .serializers import CategorySerializer
from rest_framework.generics import *
from rest_framework import permissions
from .mixins import *
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend,filters




class MyPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class UserCreateView(LoginRequiredMixin, CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


class ProductCreateView(AdminPermissionMixin, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class TableCreateView(CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


# class UserListView(ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


# class UserUpdateView(UpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class TableUpdateView(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


# class UserDelView(DestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


class ProductDelView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TableDelView(DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDelView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDelView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CookOrderView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = CookOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['cooked']


class CookOrderUpdate(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = CookOrderUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderReportView(ListAPIView):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = OrderSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['created_at']
    search_fields = ['created_at']
