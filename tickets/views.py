# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
)
from rest_framework import viewsets
from models import (
    Ticket,
)
from serializers import (
    TicketSerializer,
    TICKET_FIELDS,
)


class TicketListView(TemplateView):
    template_name = 'tickets/list.html'


class TicketCreateView(CreateView):
    model = Ticket
    fields = TICKET_FIELDS
    template_name = 'tickets/create.html'
    success_url = '/tickets/list'


class TicketViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
