from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)


@admin.register(Category)
class Datatypes(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.get_fields() if not field.many_to_many]


@admin.register(Post)
class Datatypes(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.get_fields() if not field.many_to_many]
    # list_display.append(Category._meta.get_field('name') )
