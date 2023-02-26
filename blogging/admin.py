from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)


@admin.register(Category)
class Datatypes(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.get_fields() if not field.many_to_many]
    # exclude = ['posts']

class PostInline(admin.StackedInline):
    model = Category.posts.through
    # fk_name = 'posts'
    # many_to_many_name = 'posts'


@admin.register(Post)
class Datatypes(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.get_fields() if not field.many_to_many]
    inlines = [PostInline]






# class PostInline(admin.StackedInline):
#     model = Category
#     fk_name = 'name'
#     raw_id_fields = ("name",)

# class PostAdmin(admin.ModelAdmin):
#     print(PostInline)
#     inlines = [
#         PostInline,
#     ]
