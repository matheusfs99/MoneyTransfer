from rest_framework import serializers
from .models import Account, TransactionHistory


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = ("id",)


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = ("value", "payer", "receiver", "datetime")
        read_only_fields = ("value", "payer", "receiver",)
