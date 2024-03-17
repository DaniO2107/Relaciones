
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #urls de one a uno

    path('uno/', include('one_to_one.urls'), name='one_to_one.urls'),
  #urls de muchos a uno
    path('dos/', include('uno_a_muchos.urls'), name='uno_a_muchos.urls'),
  #urls de mucho a muchos 

    path('tes/', include('muchos_a_muchos.urls'), name='muchos_a_muchos.urls'),

]
