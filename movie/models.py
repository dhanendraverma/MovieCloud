from django.db import models

# Create your models here.

class movie(models.Model):
	movie_name =  models.CharField(max_length=200)
	last_updated = models.DateTimeField(auto_now_add=True)
	poster = models.ImageField(upload_to='image')
	word_cloud = models.ImageField(upload_to='image')

	def __str__(self):
		return self.movie_name