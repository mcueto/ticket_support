from rest_framework import serializers
from models import (
    Ticket,
)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'code',
            'title',
            'description',
            'current_status',
            'created_at',
            'updated_at',
        )
