from django.conf.urls import url, include
from views import (
    TicketListView,
    TicketCreateView,
)


urlpatterns = [
    url(r'list', TicketListView.as_view(), name='tickets_list'),
    url(r'create', TicketCreateView.as_view(), name='tickets_create'),
]
