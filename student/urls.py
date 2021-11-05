
from django.urls import path
from .import views


urlpatterns = [
    
    path('', views.Student_Details, name='Student_Details'),
    path('pdf/',views.pdf_page, name='pdf')

]
