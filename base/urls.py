from django.urls import path
from . import views
urlpatterns = [
    path('auth/register/',views.RegisterView.as_view()),
    path('auth/login/',views.LoginView.as_view()),
    path('patients/',views.PatientView.as_view()),
    path('patients/<uuid:pk>/',views.PatientView.as_view()),
    path('doctors/',views.DoctorView.as_view()),
    path('doctors/<uuid:pk>/',views.DoctorView.as_view()),
    path('mappings/',views.MappingCreateView.as_view()),
    path('mappings/<uuid:patient_id>/',views.MappingCreateView.as_view()),
    path('mappings/<uuid:pk>/',views.MappingDeleteView.as_view()),

]
