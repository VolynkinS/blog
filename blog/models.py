from django.db import models

'''
Category
==============
title, slug

Tag
==============
title, slug

Post
==============
title, slug, author, content, photo, views, category, tags, created_at
'''


class CommonInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=80, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['title']


class Category(CommonInfo):
    class Meta(CommonInfo.Meta):
        verbose_name_plural = 'Categories'


class Tag(CommonInfo):
    class Meta(CommonInfo.Meta):
        verbose_name_plural = 'Tags'


class Post(CommonInfo):
    author = models.CharField(max_length=100, verbose_name='Author')
    content = models.TextField(verbose_name='Content')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                              verbose_name='Photo')
    views = models.IntegerField(default=0, verbose_name='Number of views')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 related_name='posts', verbose_name='Category')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts',
                                  verbose_name='Tags')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Posts'
