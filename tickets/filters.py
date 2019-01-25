from django_filters import rest_framework as filters
from models import (
    Ticket,
)


class TicketFilter(filters.FilterSet):

    class Meta:
        model = Ticket
        fields = (
            '__all__'
        )
