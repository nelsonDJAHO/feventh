from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [

	path('', views.indexView, name='index'),
	path('about/', views.aboutCompanyView, name='aboutCompanyView'),
	path('team/', views.teamView, name='teamView'),
	path('services/', views.servicesView, name='services'),
	path('servicesdetails/<int:id>/', views.serviceDetailsView, name='servicesdetails'),
	path('projects/', views.projectsView, name='projects'),
	path('projectsdetails/<int:id>/', views.projectsDetailsView, name='projectdetails'),
	path('contact/', views.contacView, name='contact'),
	path('newsLetterSubscribtion/', views.newsLetterSubscribtion, name='newsLetterSubscribtion'),
	path('contactForm/', views.contactForm, name='contactForm'),
]