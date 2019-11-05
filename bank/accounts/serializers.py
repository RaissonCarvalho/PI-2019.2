from rest_framework import serializers
from accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('owner', 'balance', 'creation_date')


    def     create(self, validated_data):
        if validated_data['balance'] < 0:
            raise serializers.ValidationError('Saldo não pode ser negativo')
        else:
            return Account.objects.create(
                owner=validated_data['owner'],
                balance=validated_data['balance'],
            )

    def update(self, instance, validated_data):
        if validated_data['balance'] > 0:
            instance.balance = instance.balance + validated_data['balance']
        elif validated_data['balance'] < 0:
            instance.balance = instance.balance + validated_data['balance']
            if instance.balance < 0:
                raise serializers.ValidationError('Insuficient balance')
        elif validated_data['balance'] == 0:
            raise serializers.ValidationError('Balance cannot be 0')
        instance.save()

        return instance