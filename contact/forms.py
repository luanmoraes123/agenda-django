from .models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Primeiro nome",
        help_text="Escreva o nome aqui."
    )
    last_name = forms.CharField(
        label="Sobrenome",
        help_text="Escreva o sobrenome aqui."
    )
    phone = forms.CharField(
        label="Telefone",
        help_text="Escreva o telefone aqui."
    )
    email = forms.CharField(
        label="Email",
        help_text="Escreva o email aqui."
    )

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category'
        )

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error('first_name',
                           ValidationError("Não use ABC nesse campo", code='invalid'))
        return first_name
