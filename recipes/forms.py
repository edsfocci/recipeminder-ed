from django import forms
import datetime

class RecipeForm(forms.Form):
  name = forms.CharField(label='name')
  created = forms.DateField(initial=datetime.date.today)
  servings = forms.IntegerField(label='servings', min_value=0)
  description = forms.CharField(label='description', widget=forms.Textarea,
    required=False)
  ingredients = forms.CharField(label='ingredients', widget=forms.Textarea,
    required=False)
  instructions = forms.CharField(label='instructions', widget=forms.Textarea,
    required=False)

