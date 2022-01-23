from django.contrib import admin

from reviews.models import Publisher, Review, Contributor, Book, BookContributor


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Review)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
