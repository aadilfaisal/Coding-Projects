from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='Login'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_personal_details/', views.add_personal_details, name='add_personal_details'),
    path('student_form/', views.student_form, name='student_form'),
    path('parent_form/', views.parent_form, name='parent_form'),
    path('faculty_form/', views.faculty_form, name='faculty_form'),
    path('transaction_form/', views.transaction_form, name='transaction_form'),
    path('view_transactions/', views.view_transactions, name='view_transactions'),
    path('logout/', views.logout_view, name='logout'),
]
