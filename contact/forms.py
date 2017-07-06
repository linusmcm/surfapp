from django import forms


class contactForm(forms.Form):
    name = forms.CharField(required=False, label='Your name', help_text='100 char max')
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)



