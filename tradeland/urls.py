"""tradeland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.index,name="home"),
    path('', views.index, name="index"),
    path('base',views.base,name="base"),
    path('addproperty',views.add_property.as_view(),name="addproperty"),
    path('updateproperty/<int:pk>',views.update_property.as_view(),name="update_property"),
    path('myproperties',views.myproperties.as_view(),name="myproperties"),
    path('properties/<int:pk>',views.view_property,name="viewproperty"),
    path('chat',views.chat,name="chat"),
    path('premium',views.premium,name="premium"),
    path('offers',views.offers,name="offers"),
    path('contact',views.contact,name="contact"),
    path('', include('django.contrib.auth.urls')),
    path('sign-up',views.sign_up,name="signup"),
    path('testing/basev3',views.basev3,name="testingbasev3"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)