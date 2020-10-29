from django.contrib import messages
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core import mail


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        # O método abaixo faz a validação dos dados do formulário
        if form.is_valid():
            # o contexto agora será o resultado da limpeza do formulário
            body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
            mail.send_mail('Confirmação de inscrição',
                            body,
                            'contato@eventex.com.br',     # remetente
                            ['contato@eventex.com.br',
                            form.cleaned_data['email']]) # lista destinatários

            messages.success(request, 'Inscrição realizada com sucesso!')
            
            return HttpResponseRedirect('/inscricao/')
        # Aqui será para quando houver um erro de validação no formulário.
        else:
            return render(request, 'subscriptions/subscription_form.html', {'form': form })
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)
