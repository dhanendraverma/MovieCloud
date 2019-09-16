from django import forms
from . import models

class movieForm(forms.ModelForm):
	class Meta:
		model =  models.Movie
		fields = __all__
