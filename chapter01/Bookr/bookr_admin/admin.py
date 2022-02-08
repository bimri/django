from django.contrib import admin
from django.contrib.admin.apps import AdminConfig

class BookrAdmin(AdminConfig):
    default_site = 'bookr_admin.admin.BookrAdmin'
    site_header = "Bookr Administration"