from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


# Register your models here.

# Company
class EmailInLine(admin.StackedInline):
    model = CompanyEmail
    extra = 1


class AdressInline(admin.StackedInline):
    model = CompanyAddress
    extra = 1


class ContactInline(admin.StackedInline):
    model = CompanyPhoneNumber
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = [EmailInLine, AdressInline, ContactInline]
    list_display = ('Name', 'Slogan', 'OfficeHour')


admin.site.register(Company, CompanyAdmin)


# User registration
class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 1


class MyUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_name', 'last_name', 'is_superuser')}),
    )


# admin.site.unregister(User)
# admin.site.register(User)
# admin.site.register(User, MyUserAdmin)


class MyTeammemberAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'Group',)
    search_fields = ['user_name']


admin.site.register(TeamMember, MyTeammemberAdmin)


# Baniere
class BaniereAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Description')
    search_fields = ['Title']
    date_hierarchy = 'Publish_date'


admin.site.register(Baniere, BaniereAdmin)


# Services and projects
class ProjectsInline(admin.StackedInline):
    model = Project
    extra = 1


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ProjectsInline]
    list_display = ('id', 'Title', 'Publish_date', 'Update_date')
    search_fields = ['Title']
    empty_value_display = '-empty-'
    date_hierarchy = 'Publish_date'


admin.site.register(Service, ServiceAdmin)


# Partner
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Website_url', 'Publish_date', 'Update_date')
    search_fields = ['Name', 'Website_url']
    empty_value_display = '-empty-'
    date_hierarchy = 'Publish_date'


admin.site.register(Partner, PartnerAdmin)


# Projects
class ProjectSummernoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('Description',)


class ProjectPosterInline(admin.StackedInline):
    model = ProjectPoster
    extra = 3


class ProjectAdmin(SummernoteModelAdmin):
    inlines = [ProjectPosterInline]
    list_display = ('Title', 'Service', 'Partner', 'publish_date')
    search_fields = ['Title', 'Service', 'Partner', 'publish_date']
    summernote_fields = ('Description',)


admin.site.register(Project, ProjectAdmin, )


# Customer
class MyCustomerAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'Gender', 'PhoneNumber',)
    search_fields = ['user_name', 'user_email', 'PhoneNumber']


admin.site.register(Customer, MyCustomerAdmin)


# COntact Form
class MyContactFormAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'Subject', 'Status', 'publish_date')
    search_fields = ['']
    list_filter = ['publish_date', 'Status']


admin.site.register(ContactForm, MyContactFormAdmin)


# Why choose us
admin.site.register(WhyChooseUs,)


# Testimonial
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('Name', 'publish_date')
    date_hierarchy = 'publish_date'


admin.site.register(Testimonial, TestimonialAdmin)
