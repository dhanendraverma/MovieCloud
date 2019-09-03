from django import forms
from . import models

class movieForm(forms.ModelForm):
	class Meta:
		model =  models.movie
		fields = '__all__'