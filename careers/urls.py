from django.urls import path
from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CareerListCreateView, CareerCategoryView, CareerRetrieveUpdateDeleteView, CustomTokenObtainPairView, home, career_detail, login_view, add_career, search_careers, about, contact, career_list, register_view, submit_contact_form, password_reset, logout_view

urlpatterns = [
    path('career/', CareerListCreateView.as_view(), name='career-list'),
    path('careers/<int:pk>/', CareerRetrieveUpdateDeleteView.as_view(), name='career-detail'),
    path('categories/', CareerCategoryView.as_view(), name='career-categories'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', home, name='home'),
    path('career/<int:pk>/', career_detail, name='career_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('password_reset/', password_reset, name='password_reset'),
    path('add-career/', add_career, name='add_career'),
    path('search/', search_careers, name='search_careers'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('careers/', career_list, name='career_list'),
    path('', lambda request: redirect('/careers/')),
    path("submit_contact_form/", submit_contact_form, name="submit_contact_form"), 
]