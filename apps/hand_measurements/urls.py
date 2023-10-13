"""
URL configuration for exarth_learning_task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from apps.hand_measurements.views import View


app_name = "hand_measurements"
urlpatterns = [

    path('', View.camera, name='camera'),
    path('save_photo', View.upload_photo, name='save_photo'),
    path('recommendations', View.recommendations, name='recommendations'),
    # path('calculate_ppi', View.calculate_ppi, name='calculate_ppi'),
    path('view_ppi', View.view_ppi, name='view_ppi'),
    path('get_frame', View.get_frame, name='get_frame'),
    path('croping', View.croping, name='croping'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)