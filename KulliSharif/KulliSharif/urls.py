"""KulliSharif URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from KulliSharifapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('KulliSharifapp.urls'))
    path('events/',views.EventsListApiView.as_view()),
    path('events/<int:pk>',views.EventsRetriveApiView.as_view,),
    path('books/',views.BooksListApiView.as_view()),
    path('books/<int:pk>',views.BooksRetriveApiView.as_view()),
    path('videos/',views.VideosListApiView.as_view()),
    path('videos/<int:pk>',views.VideosRetriveApiView.as_view()),
    path('projects/',views.ProjectsListApiView.as_view()),
    path('projects/<int:pk>',views.ProjectsRetriveApiView.as_view())
]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
