from rest_framework import serializers
from users.models import Wallet


class WalletSerializers(serializers.Serializer):
    class Meta:
        model = Wallet 
        fields = ('amount', 'date')
        read_only_fields = ("id")

    def get_cat(self, obj):
        return obj.amount