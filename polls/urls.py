from django.urls import path
from . import views

app_name = 'polls'  # Naming your booth

urlpatterns = [
    path('', views.index, name='index'),  # The entrance of your booth
    path('<int:question_id>/', views.detail, name='detail'),  # Detailed question page
    path('<int:question_id>/results/', views.results, name='results'),  # Results section
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Voting area
]
