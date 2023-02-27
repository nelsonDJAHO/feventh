from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from validate_email import validate_email

from .models import *


# Create your views here.

# Index view
def indexView(request):
	if not Company.objects.all():
		Company.objects.create(
			Name="FEVENTH",
			Slogan='TECH & BEYOND',
			OfficeHour='08:00 - 17:00',
			CompanyAbout='CompanyAbout',
			CompanyMission='CompanyMission',
			CompanyVision='CompanyVision',
		)

	company = Company.objects.first()
	firstCompanyAdress = CompanyAddress.objects.filter(Company_id=company.id)[:1]
	firstCompanyEmail = CompanyEmail.objects.filter(Company_id=company.id)[:1]
	firstCompanyContact = CompanyPhoneNumber.objects.filter(Company_id=company.id)[:3]
	banieres = Baniere.objects.all()
	services = Service.objects.all()[:6]
	projects = Project.objects.all()
	completedprojects = Project.objects.filter(Status='Completed').count()
	remainingprojects = Project.objects.filter(Status='Remaining').count()
	partners = Partner.objects.all()
	testimonials = Testimonial.objects.all()
	context = {
		'company': company,
		'firstCompanyAdress':firstCompanyAdress,
		'firstCompanyEmail':firstCompanyEmail,
		'firstCompanyContact': firstCompanyContact,
		'banieres': banieres,
		'services': services,
		'projects': projects,
		'partners': partners,
		'completedprojects': completedprojects,
		'remainingprojects': remainingprojects,
		'testimonials': testimonials

	}
	return render(request, 'main/index.html', context)


# About us
def aboutCompanyView(request):
	company = Company.objects.first()
	services = Service.objects.all()[:6]
	firstCompanyAdress = CompanyAddress.objects.filter(Company_id=company.id)[:1]
	firstCompanyEmail = CompanyEmail.objects.filter(Company_id=company.id)[:1]
	firstCompanyContact = CompanyPhoneNumber.objects.filter(Company_id=company.id)[:3]
	whychooseus = WhyChooseUs.objects.all()
	firstwhychooseusid = whychooseus.first().id
	context = {
		'company': company,
		'services': services,
		'firstCompanyAdress': firstCompanyAdress,
		'firstCompanyEmail': firstCompanyEmail,
		'firstCompanyContact': firstCompanyContact,
		'whychooseus': whychooseus,
		'firstwhychooseusid': firstwhychooseusid
	}
	return render(request, 'main/about.html', context)


# About us
def teamView(request):
	company = Company.objects.first()
	services = Service.objects.all()[:6]
	persons = TeamMember.objects.all()
	firstCompanyAdress = CompanyAddress.objects.filter(Company_id=company.id)[:1]
	firstCompanyEmail = CompanyEmail.objects.filter(Company_id=company.id)[:1]
	firstCompanyContact = CompanyPhoneNumber.objects.filter(Company_id=company.id)[:3]
	context = {
		'company': company,
		'firstCompanyAdress': firstCompanyAdress,
		'firstCompanyEmail': firstCompanyEmail,
		'firstCompanyContact': firstCompanyContact,
		'services': services,
		'persons': persons,
	}
	return render(request, 'main/team.html', context)


# Services
def servicesView(request):
	company = Company.objects.first()
	firstCompanyAdress = CompanyAddress.objects.filter(Company_id=company.id)[:1]
	firstCompanyEmail = CompanyEmail.objects.filter(Company_id=company.id)[:1]
	firstCompanyContact = CompanyPhoneNumber.objects.filter(Company_id=company.id)[:3]
	services = Service.objects.all()
	context = {
		'company': company,
		'firstCompanyAdress': firstCompanyAdress,
		'firstCompanyEmail': firstCompanyEmail,
		'firstCompanyContact': firstCompanyContact,
		'services': services,
	}
	return render(request, 'main/services.html', context)


# Service details
def serviceDetailsView(request, id):
	company = Company.objects.first()
	firstCompanyAdress = CompanyAddress.objects.filter(Company_id=company.id)[:1]
	firstCompanyEmail = CompanyEmail.objects.filter(Company_id=company.id)[:1]
	firstCompanyContact = CompanyPhoneNumber.objects.filter(Company_id=company.id)[:3]
	services = Service.objects.all()[:6]
	services1 = Service.objects.all()
	service = get_object_or_404(Service, id=id)
	completedprojects = Project.objects.filter(Status='Completed', Service_id=id).count()
	remainingprojects = Project.objects.filter(Status='Remaining', Service_id=id).count()
	team = TeamMember.objects.filter(Service__id=id).count()
	context = {
		'company': company,
		'firstCompanyAdress': firstCompanyAdress,
		'firstCompanyEmail': firstCompanyEmail,
		'firstCompanyContact': firstCompanyContact,
		'services': services,
		'services1': services1,
		'service': service,
		'team': team,
		'completedprojects': completedprojects,
		'remainingprojects': remainingprojects,
	}
	return render(request, 'main/servicedetails.html', context)


# Projects
def projectsView(request):
	company = Company.objects.first()
	firstCompanyAdress = CompanyAddress.objects.filter(Company_id=company.id)[:1]
	firstCompanyEmail = CompanyEmail.objects.filter(Company_id=company.id)[:1]
	firstCompanyContact = CompanyPhoneNumber.objects.filter(Company_id=company.id)[:3]
	services = Service.objects.all()
	projects = Project.objects.all()
	context = {
		'company': company,
		'firstCompanyAdress': firstCompanyAdress,
		'firstCompanyEmail': firstCompanyEmail,
		'firstCompanyContact': firstCompanyContact,
		'services': services,
		'projects': projects,
	}
	return render(request, 'main/projects.html', context)


# Projects details
def projectsDetailsView(request, id):
	company = Company.objects.first()
	firstCompanyAdress = CompanyAddress.objects.filter(Company_id=company.id)[:1]
	firstCompanyEmail = CompanyEmail.objects.filter(Company_id=company.id)[:1]
	firstCompanyContact = CompanyPhoneNumber.objects.filter(Company_id=company.id)[:3]
	services = Service.objects.all()
	project = get_object_or_404(Project, id=id)
	similarProjects = Project.objects.filter(Service_id=project.Service_id).exclude(id=project.id)
	context = {
		'company': company,
		'firstCompanyAdress': firstCompanyAdress,
		'firstCompanyEmail': firstCompanyEmail,
		'firstCompanyContact': firstCompanyContact,
		'services': services,
		'project': project,
		'similarProjects': similarProjects
	}
	return render(request, 'main/projectdetails.html', context)


# Contact
def contacView(request):
	company = Company.objects.first()
	services = Service.objects.all()[:6]
	firstCompanyAdress = CompanyAddress.objects.filter(Company_id=company.id)[:1]
	companyAddresses = CompanyAddress.objects.filter(Company_id=company.id)
	firstCompanyEmail = CompanyEmail.objects.filter(Company_id=company.id)[:1]
	companyEmails = CompanyEmail.objects.filter(Company_id=company.id)
	firstCompanyContact = CompanyPhoneNumber.objects.filter(Company_id=company.id)[:3]
	companyContacts = CompanyPhoneNumber.objects.filter(Company_id=company.id)
	context = {
		'company': company,
		'firstCompanyAdress': firstCompanyAdress,
		'companyAddresses': companyAddresses,
		'firstCompanyEmail': firstCompanyEmail,
		'companyEmails': companyEmails,
		'firstCompanyContact': firstCompanyContact,
		'companyContacts': companyContacts,
		'services': services,
	}
	return render(request, 'main/contact.html', context)


# News letter subscribtion
def newsLetterSubscribtion(request):
	status = True
	message = "Inscription faite"

	emailAdress = request.POST.get('emailAdress')

	if not emailAdress:
		status = False
		message = "Veuillez fournir votre addresse mail"
	elif not validate_email(emailAdress):
		status = False
		message = "Veuillez saisir une adresse email valide"
	elif User.objects.filter(email=emailAdress).exists():
		status = False
		message = "Vous êtes déjà abonné(e), merci pour votre interêt."
	else:
		newCustomer = User.objects.create_user(username=emailAdress, email=emailAdress, password=emailAdress)
		if newCustomer:
			Customer.objects.create(User_id=newCustomer.id)

	return JsonResponse({'status': status, 'message': message})


# Contact form
def contactForm(request):

	status = True
	message = "Votre message a été enregistré, nous vous revenons dans les plus brefs délais"

	last_name = request.POST.get('last_name')
	first_name = request.POST.get('first_name')
	email = request.POST.get('email')
	phone = request.POST.get('phone')
	subject = request.POST.get('subject')
	messageText = request.POST.get('message')

	if not last_name:
		status = False
		message = "Veuillez préciser votre nom"
	elif not first_name:
		status = False
		message = "Veuillez préciser votre prénom"
	elif not email:
		status = False
		message = "Veuillez préciser votre email"
	elif not validate_email(email):
		status = False
		message = "Veuillez saisir une adresse email valide"
	elif not phone:
		status = False
		message = "Veuillez préciser votre numéro de téléphone"
	elif not subject:
		status = False
		message = "Veuillez préciser le sujet de votre message"
	elif not messageText:
		status = False
		message = "Veuillez préciser votre message"
	else:
		# Rechercher l utilisateur par l email
		if User.objects.filter(email__exact=email).exists():
			oldUser = User.objects.get(email__exact=email)
			oldUser.last_name = last_name
			oldUser.first_name = first_name
			oldUser.save()

			customer = Customer.objects.get(User_id=oldUser.id)
			customer.PhoneNumber = phone
			customer.save()

			ContactForm.objects.create(Customer_id=customer.id, Subject=subject, message=messageText, Status='Unread')

		else:
			newUser = User.objects.create_user(username=email, email=email, password=email, last_name=last_name, first_name=first_name)
			if newUser:
				newCustomer = Customer.objects.create(User_id=newUser.id, PhoneNumber=phone)
				if newCustomer:
					ContactForm.objects.create(Customer_id=newCustomer.id, Subject=subject, message=messageText, Status='Unread')

		return JsonResponse({'status': status, 'message': message})
