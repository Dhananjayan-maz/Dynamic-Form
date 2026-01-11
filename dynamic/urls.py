"""
URL configuration for dynamic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views 

from django .conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("__reload__/", include("django_browser_reload.urls")), 

    path('create_form/', views.create_form, name='create_form'),
    path("register/<slug:slug>/", views.registration_view, name="register_form"),
    path('entries_list/', views.entries_list, name='entries_list'),
    path("entries/<slug:slug>/", views.view_entries, name="view_entries"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path("forms/<int:id>/delete/", views.delete_form, name="delete_form"),
    path( "entries/update/<slug:slug>/<int:entry_id>/", views.update_register,name="update_register"),

]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 