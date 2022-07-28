from api.models import Mailing, Client, Message, Operator, Tag


def get_mailing_queryset():
    queryset = Mailing.objects.all()
    return queryset


def get_clients_queryset():
    queryset = Client.objects.all()
    return queryset


def get_messages_queryset():
    queryset = Message.objects.all()
    return queryset


def get_operators_queryset():
    queryset = Operator.objects.all()
    return queryset


def get_tags_queryset():
    queryset = Tag.objects.all()
    return queryset
