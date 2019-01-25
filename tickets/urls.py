from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from views import (
    TicketListView,
    TicketCreateView,
    TicketViewSet,
)

router = DefaultRouter()

router.register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    url(r'list', TicketListView.as_view(), name='tickets_list'),
    url(r'create', TicketCreateView.as_view(), name='tickets_create'),
    url(r'api/', include(router.urls)),
]
