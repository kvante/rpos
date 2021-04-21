from django.urls import include, path
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register(r'item', views.UserViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.urls import path

from . import views

app_name = 'rpos'

urlpatterns = [
    #path('api/v1/User', views.UserViewSet.as_view(), name='get_User'),
    path('api/v1/UsersList', views.UserListView.as_view(), name='get_post_User'),
    path('api/v1/UserCreate', views.UserCreateView.as_view(), name='set_post_User'),
    path('api/v1/UserDel', views.UserDelView.as_view(), name='del_post_User'),
    path('api/v1/UserUpdate', views.UserUpdateView.as_view(), name='update_post_User'),

    path('api/v1/CategorytList', views.CategoryListView.as_view(), name='get_post_Category'),
    path('api/v1/CategoryCreate', views.CategoryCreateView.as_view(), name='get_post_Category'),
    path('api/v1/CategoryDel', views.CategoryDelView.as_view(), name='del_post_Category'),
    path('api/v1/CategoryUpdate', views.CategoryUpdateView.as_view(), name='update_post_Category'),

    path('api/v1/ProductList', views.ProductListView.as_view(), name='get_post_Product'),
    path('api/v1/ProductCreate', views.ProductCreateView.as_view(), name='get_post_Product'),
    path('api/v1/ProductDel', views.ProductDelView.as_view(), name='del_post_Product'),
    path('api/v1/ProductUpdate', views.ProductUpdateView.as_view(), name='update_post_Product'),

    path('api/v1/TableList', views.TableListView.as_view(), name='get_post_Table'),
    path('api/v1/TableCreate', views.TableCreateView.as_view(), name='get_post_Table'),
    path('api/v1/TableDel', views.TableDelView.as_view(), name='del_post_Table'),
    path('api/v1/TableUpdate', views.TableUpdateView.as_view(), name='update_post_Table'),

    path('api/v1/OrderList', views.OrderListView.as_view(), name='get_post_Order'),
    path('api/v1/OrderCreate', views.OrderCreateView.as_view(), name='get_post_Order'),
    path('api/v1/OrderDel', views.OrderDelView.as_view(), name='del_post_Order'),
    path('api/v1/OrderUpdate', views.OrderUpdateView.as_view(), name='update_post_Order'),


]