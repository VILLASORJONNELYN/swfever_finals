from os import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'sfsys'
urlpatterns = [
    path('',views.Homepage, name="homepage"),
    path('Tablelist/',views.Tablelist, name="Tablelist"),
    path('Swfrecordslist/',views.Swfrecordslist, name="Swfrecordslist"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete1/<int:id>', views.delete1, name='delete1'),
    path('updates1/<int:id>', views.updates1, name='updates1'),

    ]