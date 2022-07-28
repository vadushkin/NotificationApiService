from rest_framework import serializers
from .models import *


class MailingSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    operators = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Mailing
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField()
    operator = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    mailing = serializers.StringRelatedField(read_only=True)
    client = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
