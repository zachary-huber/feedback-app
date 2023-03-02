from django.contrib import admin

# Register your models here.

from .models import Project, Review, Tag, Form, Response

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)



admin.site.register(Form)
admin.site.register(Response)