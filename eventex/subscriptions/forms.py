from django import forms
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        words = self.cleaned_data['name'].split()
        titled_words = [word.title() for word in words]
        return " ".join(titled_words)

    def clean(self):
        # esta primeira linha garante que estará chamando também o clean do ModelForm
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu email ou telefone')

        return self.cleaned_data
