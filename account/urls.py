from django.urls import path
from knox import views as knox_views
from . import api
from . import views


urlpatterns = [
    path('register/', api.RegisterAPI.as_view(), name='register'),
    path('login/', api.LoginAPI.as_view(), name='login'),
    path('user/', api.UserAPI.as_view(), name='user'),
    # path('updateUser/', api.UpdateUserApi.as_view(), name='user'),

    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('change-password/', api.ChangePasswordView.as_view(),
         name='change-password'),


    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>', views.get_update_delete_user, name='user'),
    path('profile/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.get_update_delete_profile, name='profile'),

]
