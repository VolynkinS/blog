from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CommonInfo(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    save_on_top = True


class CategoryAdmin(CommonInfo):
    pass


class TagAdmin(CommonInfo):
    pass


class PostAdmin(CommonInfo):
    form = PostAdminForm
    list_display = ('id', 'title', 'slug', 'created_at', 'category', 'get_photo')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="80"')

    get_photo.short_description = 'Photo'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
