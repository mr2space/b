# forms.py

from django import forms
from .models import Photos

class FamilyPhotosForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['photo', 'category']

    def __init__(self, *args, **kwargs):
        super(FamilyPhotosForm, self).__init__(*args, **kwargs)
        # You can customize the form fields here if needed

    # You can add additional form-level validation or customization methods here if needed
