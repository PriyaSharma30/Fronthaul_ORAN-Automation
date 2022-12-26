"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('FH.urls'))
# ]
from django.urls import path, include
from django.contrib import admin
# from django.conf.urls import url
from django.contrib import admin
# from . import views
from FH import views

urlpatterns = [


##### for configuration Page #########
    path('admin/', admin.site.urls),
    path('', include('FH.urls')),
    path('', views.home,name="script"),
    # path('button/',views.button),
    ##### for base_dl Page #########
    path('about', views.about),
    path('about1', views.about1),
    path("base",views.base,name="script"),
    path("base1",views.base1,name="script"),
    path('external', views.external),
    path('cu_base_dl', views.cu_base_dl),

    ##### for extended_dl Page #########
    path('extended', views.extended),
    path("extended_run",views.extended_run,name="script"),
    path('extended1', views.extended1),
    path("extended_run1",views.extended_run1,name="script"),
    # path('cu', views.cu),
    path('CU_extended_dl', views.CU_extended_dl),
    
   
    
]



