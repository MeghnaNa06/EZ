from unicodedata import name
from  django.urls import path , include
from rest_framework.urlpatterns import format_suffix_patterns
from.import views
from .views import Display_Image, index

urlpatterns = [
    path('',views.PersonView.as_view()),
    path('delete/',views.Details.as_view()),
    path('image/',index , name="Image" ),
    
    path('display_image/',Display_Image , name="Image" ),

    path('add/',views.Details.as_view())
]
