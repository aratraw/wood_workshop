from django.contrib import admin
from .models import Project, Category, ShopItem, Image, Tag
# Register your models here.


admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(ShopItem)
""" class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


admin.site.register(Project, ProjectAdmin) """
