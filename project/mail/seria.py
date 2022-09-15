from rest_framework import serializers
from .models import Mailing, Client, Message


class MailSeria(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"


class ClientSeria(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class MessageSeria(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'