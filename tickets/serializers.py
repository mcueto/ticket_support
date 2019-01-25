from rest_framework import serializers
from models import (
    Ticket,
)


TICKET_FIELDS = (
    'code',
    'title',
    'description',
    'current_status',
    'created_at',
    # 'updated_at',
)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = TICKET_FIELDS
