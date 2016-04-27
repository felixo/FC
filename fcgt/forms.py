from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def handle_uploaded_file(f):
    destination = open('images/name.jpg', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()