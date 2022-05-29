from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=64)
    change_balance_value = serializers.FloatField(required=False)

    class Meta:
        model = Client
        fields = ['username', 'password', 'change_balance_value']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_change_balance_value(self, value):
        if self.instance.balance_value + value < 0:
            serializers.ValidationError("Balance should be positive.")
        return value

    def save(self, **kwargs):
        username = self.validated_data.get('username')
        password = self.validated_data.get('password')
        if username and password:
            client = Client(
                username=self.validated_data['username'],
            )

            password = self.validated_data['password']
            client.set_password(password)
        return super().save(**kwargs)

    def update(self, instance, validated_data):
        instance.balance_value += self.validated_data.get('change_balance_value', 0)
        instance.save()
        return instance
