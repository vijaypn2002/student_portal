from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_login, name='student_login'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('view-result/', views.view_result, name='view_result'),
    path('download-hallticket/', views.download_hallticket, name='download_hallticket'),
    path('download-hallticket-pdf/', views.generate_hallticket_pdf, name='download_hallticket_pdf'),
    path('download-result/', views.download_result, name='download_result'),
    path('bulk-upload-results/', views.bulk_upload_results, name='bulk_upload_results'),
    path('bulk-upload-halltickets/', views.bulk_upload_halltickets, name='bulk_upload_halltickets'),
]
