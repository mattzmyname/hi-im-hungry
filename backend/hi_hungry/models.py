from django.db import models


class User(models.Model):
	name = models.CharField(max_length=50)
	rating = models.IntegerField()
	
	def __str__(self):
		return self.name


class restaurant(models.Model):
	"""Model representing a book (but not a specific copy of a book)."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		"""String for representing the Model object."""
		return self.name