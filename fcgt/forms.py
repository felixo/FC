from django import forms

class ImageUploadForm(forms.Form):
    image = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )