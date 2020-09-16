from django.contrib import admin
from django.urls import path
from . import views
app_name="timeline"

urlpatterns = [
    path('dashboard/',views.dashboard, name="dashboard"),
    path('addtimeline/',views.addtimeline, name="addtimeline"),
    path('timeline/<int:id>',views.detail, name="detail"),
    path('update/<int:id>',views.updatetimeline, name="update"),
    path('delete/<int:id>',views.deletetimeline, name="delete"),
    path('',views.timelines, name="timelines"),
    path('comment/<int:id>',views.comment, name="comment"),
]
