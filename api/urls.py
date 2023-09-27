from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.getAngeschlosseneGereate),
    path('hmp4040_measure/',views.hmp4040_measure),
    path('hmp4040_auto_corrector/',views.hmp4040_auto_corrector),
    path('channel_aktivieren/',views.channel_aktivieren) ,
    path('channel_deaktivieren/',views.channel_deaktivieren) ,
    path('out_aktivieren/',views.out_aktivieren) ,
    path('out_deaktivieren/',views.out_deaktivieren) 
]
