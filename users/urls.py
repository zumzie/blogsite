from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView, CustomLogoutView
from rest_framework import routers

router = routers.DefaultRouter()
#router.register(r'users', UserViewSet())


urlpatterns= [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(template_name='users/signup.html'), name='signup'),
#   path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]