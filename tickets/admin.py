# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import (
    Ticket,
)


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'title',
        'current_status',
        'created_at'
    )
    list_filter = (
        'code',
        'current_status',
    )
    search_fields = (
        'code',
        'title',
        'description',
        'current_status',
        'created_at',
    )


admin.site.register(Ticket, TicketAdmin)
