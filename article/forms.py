from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField()
    name = forms.CharField()
    subject = forms.CharField()
    message = forms.Textarea()

    widgets = {
        'from_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'subject': forms.Select(attrs={'class': 'form-control'}),
        'message': forms.Textarea(attrs={'class': 'form-control'})
    }
