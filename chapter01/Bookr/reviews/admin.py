from django.contrib import AdminSite

from reviews.models import Publisher, Review, Contributor, Book, BookContributor


class BookrAdminSite(AdminSite):
    title_header = "Bookr Admin"
    site_header = "Bookr Administration"
    index_title = "Bookr site admin"


admin_site = BookrAdminSite(name="bookr")


# Register your models here.
admin_site.site.register(Publisher)
admin_site.site.register(Review)
admin_site.site.register(Contributor)
admin_site.site.register(Book)
admin_site.site.register(BookContributor)
