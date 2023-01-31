from django import forms
from .models import employee,product

class textinput(forms.Form):
    text = forms.CharField()

class employeeForm (forms.ModelForm):
    class Meta:
        model= employee
        fields = "__all__"

class productForm (forms.ModelForm):
    class Meta:
        model= product
        fields = "__all__"
        

from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('real_image', 'mask_image')
