from django import forms
from .models import Photo
#DataFlair
class PhotoCreate(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'