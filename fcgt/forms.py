from models import Gallery
from django import forms


class ArtForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('art_host_name', 'art_city', 'art_mail', 'art_link',
                  'art_category', 'docfile')
