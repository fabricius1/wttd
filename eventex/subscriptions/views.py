from django.shortcuts import render, resolve_url as r
from eventex.subscriptions.forms import SubscriptionForm
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, Http404
from django.core import mail
from django.conf import settings
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)
    return empty_form(request)


def empty_form(request):
    return render(request,
                  'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    # forma nova, usando o método .save() do ModelForm:
    subscription = form.save()

    # forma antiga para o salvamento anterior, sem ModelForm:
    #subscription = Subscription.objects.create(**form.cleaned_data)

    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404
    return render(request,
                  'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


def _send_mail(subject, email_from, email_to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, email_from, [email_from, email_to])
