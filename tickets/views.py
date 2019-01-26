# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
)
from rest_framework import viewsets
from models import (
    Ticket,
)
from filters import (
    TicketFilter,
)
from serializers import (
    TicketSerializer,
    TICKET_FIELDS,
)


class TicketListView(LoginRequiredMixin, TemplateView):
    template_name = 'tickets/list.html'

    def get_context_data(self, **kwargs):
        context = super(TicketListView, self).get_context_data(**kwargs)

        context['api_base_url'] = self.request.build_absolute_uri('api')
        return context


class TicketCreateView(PermissionRequiredMixin, CreateView):
    model = Ticket
    fields = TICKET_FIELDS
    template_name = 'tickets/create.html'
    success_url = '/tickets/list'
    permission_required = 'tickets.add_ticket'


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all().order_by('-created_at')
    filter_class = TicketFilter
