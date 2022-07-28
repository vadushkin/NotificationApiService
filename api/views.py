from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .services import *
from .serializers import *


def home_page(request):
    return render(request, 'api/home.html', context={'title': 'Шарик'})


class MailingViewSet(viewsets.ModelViewSet):
    queryset = get_mailing_queryset()
    serializer_class = MailingSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('operators', 'tags')


class ClientViewSet(viewsets.ModelViewSet):
    queryset = get_clients_queryset()
    serializer_class = ClientSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = get_messages_queryset()
    serializer_class = MessageSerializer


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = get_tags_queryset()
    serializer_class = OperatorSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = get_tags_queryset()
    serializer_class = TagSerializer
