# -*- encoding: UTF-8 -*-
import logging

from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django import http
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context

from apps.gateway import forms
from oscar.apps.customer.forms import generate_username
from oscar.defaults import OSCAR_FROM_EMAIL

logger = logging.getLogger('gateway')

class GatewayView(generic.FormView):
    template_name = 'gateway/form.html'
    form_class = forms.GatewayForm



    def form_valid(self, form):
        real_email = form.cleaned_data['email']
        username = real_email
        password = generate_username()
        email = real_email

        user = self.create_dashboard_user(username, email, password)
        self.send_confirmation_email(real_email, user, password)
        logger.info("Created dashboard user #%d for %s",
            user.id, real_email)

        messages.success(
            self.request,
            u"Данные для доступа к админке магазина отправлены на email %s" % real_email)
        return http.HttpResponseRedirect(reverse('gateway'))

    def create_dashboard_user(self, username, email, password):
        user = User.objects.create_user(username, email, password)
        user.is_staff = True
        user.save()
        return user


    def send_confirmation_email(self, real_email, user, password):
        msg = get_template('gateway/email.txt').render(Context({
            'email': user.email,
            'password': password
        }))
        send_mail(u'Доступ в админку',
            msg, OSCAR_FROM_EMAIL,
            [real_email])

