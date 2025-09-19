from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class PostCategory(models.Model):
	card_img = models.CharField(max_length=300,default=1)
	post_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.SlugField(max_length=200,default=1)
	class Meta:
		verbose_name ="Category"
		verbose_name_plural = "Categories"
	def ___str__(self):
		return self.post_category
class PostSeries(models.Model):
	post_series = models.CharField(max_length=200)
	post_category = models.ForeignKey(PostCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)
	post_slug = models.SlugField(max_length=200,default=1)
	class Meta:
		verbose_name_plural = "Series"
	def __str__(self):
		return self.post_series
class Post(models.Model):
    post_series = models.ForeignKey(PostSeries,verbose_name="series",null=True,blank=False,on_delete=models.SET_NULL)
    post_slug = models.SlugField(max_length=200,default=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
   
