from rest_framework import serializers
from users.models import Wallet, User


class WalletSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Wallet
        fields = ('id', 'user', 'hamyon_raqami', 'is_active')
        read_only_fields = ('id', 'hamyon_raqami', 'is_active')