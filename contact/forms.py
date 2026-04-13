from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56 9 XXXX XXXX'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tu mensaje'}),
        }
        labels = {
            'name': 'Nombre Completo',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
            'message': 'Mensaje',
        }
