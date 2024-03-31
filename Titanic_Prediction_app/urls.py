from django.contrib import admin
from django.urls import path
from Titanic_Prediction_app import views
urlpatterns = [
    path('',views.home_view,name='home'),
    path('predict/',views.predict_survival,name='predict')
]
