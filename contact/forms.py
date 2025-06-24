from .models import Contact
from django import forms


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
    description = forms.CharField(
        label="Descrição",
        help_text="Escreva a descrição aqui."
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
            'description'
        )
