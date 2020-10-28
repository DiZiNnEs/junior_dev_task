from django.urls import path

from university import views

urlpatterns = [
    path('', views.main, name='index'),
    path('university/<str:pk>', views.university_page_delete, name='university_page'),
    path('register', views.register_page, name='register_page'),
    path('sign-in', views.login_page, name='authorization_page'),
    path('logout', views.logout_user, name='logout'),
]
