from django.urls import path
from . import views


# app_name helps to differentiate between blog app and poll ap urls of the same name.
app_name = 'polls'
# Add url paths for imported views to access in browser.
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
   
]