

from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    # path('admin/', admin.site.urls),
##### for configuration Page #########
    path("",views.home, name = "App"),
    # path("button",views.button),
    ##### for base _ dl Page ######
    path("about",views.about,name= "Hi"),
    path("about",views.about1,name= "Hi"),
    path("base",views.base,name= "Hi"),
    path("bas1",views.base,name= "Hi"),
    path("external",views.external,name= "Hi"),
    path("cu_base_dl",views.cu_base_dl,name= "Hi"),

##### for extended_dl Page #########
    path("extended",views.extended,name= "Hi"),
    path("extended_run",views.extended_run,name= "Hi"),
    path("extended1",views.extended1,name= "Hi"),
    path("extended_run1",views.extended_run1,name= "Hi"),
    path("cu",views.cu,name= "Hi"),
    path("CU_extended_dl",views.CU_extended_dl,name= "Hi"),
    
    
    
]
