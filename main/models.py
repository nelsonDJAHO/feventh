from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.

# Company
class Company(models.Model):
    Name = models.CharField(max_length=30)
    Slogan = models.CharField(max_length=50)
    OfficeHour = models.CharField(max_length=15)
    CompanyLogo = models.ImageField(upload_to='CompanyLogo/')
    CompanyAbout = models.TextField(max_length=500)
    CompanyMission = models.TextField(max_length=500)
    CompanyVision = models.TextField(max_length=500)
    Publish_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Entreprise'


class CompanyEmail(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Email = models.CharField(max_length=150)
    Publish_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Emails Entreprise'


class CompanyPhoneNumber(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length=150)
    whatsapp = models.BooleanField(default=False)
    Publish_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Contacts Entreprise'


class CompanyAddress(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Address = models.CharField(max_length=150)
    Publish_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Adresses Entreprise'


# Why choose us
class WhyChooseUs(models.Model):
    Title = models.CharField(max_length=25)
    Description = models.TextField()
    Publish_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Title


# Baniere
class Baniere(models.Model):
    Title = models.CharField(max_length=25)
    Description = models.CharField(max_length=50)
    Baniere = models.ImageField(upload_to='Banieres/')
    Publish_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Banieres'

    def __str__(self):
        return self.Title


# Partner
class Partner(models.Model):
    Name = models.CharField(max_length=30, null=False, unique=True)
    Logo = models.ImageField(upload_to="partners/", null=False)
    Website_url = models.URLField(blank=True, null=True)
    Publish_date = models.DateTimeField(auto_now_add=True)
    Update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Partenaires'

    def __str__(self):
        return self.Name


# Service
class Service(models.Model):
    Title = models.CharField(max_length=50, null=False)
    Description = models.TextField(null=False)
    Poster = models.ImageField(upload_to="Services/", null=False)
    Publish_date = models.DateTimeField(auto_now_add=True)
    Update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.Title


class Project(models.Model):
    Status_Choices = [
        ('Completed', 'Completed'),
        ('Remaining', 'Remaining')
    ]

    Service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Description = models.TextField(null=False)
    Poster = models.ImageField(upload_to="Projects/", null=False)
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)
    Status = models.CharField(max_length=20, choices=Status_Choices)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.Title


class ProjectPoster(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Poster = models.ImageField(upload_to="Projects/", null=False)
    publish_date = models.DateTimeField(auto_now_add=True)


# # Person
class TeamMember(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)
    Service = models.ManyToManyField(Service)
    Avatar = models.ImageField(upload_to="TeamMembers/", null=True, default="avatar.png")
    FacebookLink = models.CharField(max_length=50, null=True, blank=True)
    TwitterLink = models.CharField(max_length=50, null=True, blank=True)
    LinkdinLink = models.CharField(max_length=50, null=True, blank=True)
    InstagramLink = models.CharField(max_length=50, null=True, blank=True)

    def user_name(self):
        return self.User.get_full_name()

    def user_email(self):
        return self.User.email


# Customer
class Customer(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Avatar = models.ImageField(upload_to="Customers/", null=True, default="avatar.png")
    BirthDate = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=6)
    PhoneNumber = models.CharField(max_length=20, null=True, blank=True)
    Adress = models.CharField(max_length=30)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.User.get_full_name()

    def user_name(self):
        if self.User.last_name or self.User.first_name:
            return self.User.get_full_name()
        else:
            return self.User

    def user_email(self):
        return self.User.email


# Contact form
class ContactForm(models.Model):
    Status_Choices = [
        ('Unread', 'Unread'),
        ('Readed', 'Readed')
    ]

    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=50)
    message = models.TextField()
    Status = models.CharField(max_length=20, choices=Status_Choices)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Messages'

    def user_name(self):
        if self.Customer.User.last_name or self.Customer.User.first_name:
            return self.Customer.User.get_full_name()
        else:
            return self.Customer.User

    def user_email(self):
        return self.Customer.User.email


# Testimonial
class Testimonial(models.Model):
    Avatar = models.ImageField(upload_to="TeamMembers/", null=True, default="avatar.png")
    Name = models.CharField(max_length=50)
    Comment = models.CharField(max_length=250)
    Work = models.CharField(max_length=25)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
