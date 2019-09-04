from django.db import models

# Create your models here.

class Movie(models.Model):
	movie_name =  models.CharField(max_length=200)
	poster = models.ImageField(upload_to='image')
	last_updated = models.DateTimeField(auto_now_add=True)
	word_cloud = models.ImageField(upload_to='image')
	tweets = models.FileField(upload_to='tweets')

	def __str__(self):
		return self.movie_name