# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView


class TicketListView(TemplateView):
    template_name = 'tickets/list.html'


class TicketCreateView(TemplateView):
    template_name = 'tickets/create.html'
