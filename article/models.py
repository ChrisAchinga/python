from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Categories
class Category(models.Model):
    name = models.CharField('Category Name', max_length=100)
    description = models.TextField('Category Description')
    image = models.ImageField('Category Image', upload_to='uploads/')

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = verbose_name
    
    def __str__(self):
       return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Article(models.Model):
    # tag
    TAGS = (
        ('main', 'Main'),
        ('featured', 'Featured')
    )
    title = models.CharField('Article Title', max_length=100)
    cover_image = models.ImageField('Cover Image', upload_to='uploads/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tag = models.CharField('Tag', choices=TAGS, max_length=20)
    body_image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    description = models.TextField()
    subheading = models.CharField('Sub Heading', max_length=100, null=False, blank=False)
    body = models.TextField('Article Body', null=False, blank=False)
    subheading1 = models.CharField('Sub Heading (optional)', max_length=100, null=True, blank=True)
    body1 = models.TextField('Article Body (optional)', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.title + ' ' + 'by' + ' ' + str(self.author)

    @property
    def imageURL(self):
        try:
            url = self.cover_image.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))
        # return reverse('home')

class News(models.Model):
    title = models.CharField('News Title', max_length=100, null=False)
    image = models.ImageField('Image', upload_to='uploads/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField('Description', null=False)
    body = models.TextField('News Body')
    date = models.DateField('Date')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.title + ' ' + 'by' + ' ' + str(self.author)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class ImageGallery(models.Model):
    image = models.ImageField(upload_to='uploads/')
    name = models.CharField('Image Name', max_length=20)
    caption = models.TextField('Image Caption')
    description = models.TextField('Description', null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Image Gallery'
        verbose_name_plural = verbose_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
