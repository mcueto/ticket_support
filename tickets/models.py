# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.utils import timezone

# Fields constants
CODE_FIELD_MAX_LENGTH = 128
NAME_FIELD_MAX_LENGTH = 128

# Ticket status field choices
TICKET_STATUS_CHOICES = (
    ('open', 'open'),
    ('pending', 'pending'),
    ('in_process', 'in_process'),
    ('resolved', 'resolved'),
    ('closed', 'closed'),
)


class Ticket(models.Model):
    """
    BaseProduct model.

    Contains the common fields between Product and ProductVariant models.
    """
    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    code = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH
    )
    title = models.CharField(
        max_length=NAME_FIELD_MAX_LENGTH
    )
    description = models.TextField(
        blank=True
    )
    current_status = models.CharField(
        max_length=CODE_FIELD_MAX_LENGTH,
        choices=TICKET_STATUS_CHOICES
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    updated_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        """Return the class instance item name in django admin."""
        return str(self.title)+" - "+str(self.created_at)
