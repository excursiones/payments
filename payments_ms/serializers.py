from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.shortcuts import get_object_or_404
from .models import *

class UserPaymentSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    price = serializers.FloatField()
    origin_account = serializers.CharField(max_length = 30)
    destination_account = serializers.CharField(max_length = 30)

    def create(self, validated_data):
        return UserPayment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.price = validated_data.get('price', instance.price)
        instance.origin_account = validated_data.get(
                                                    'origin_account',
                                                    instance.origin_account
                                                    )
        instance.destination_account = validated_data.get(
                                                    'destination_account',
                                                    instance.destination_account
                                                    )

        instance.save()
        return instance

    class Meta:
        model = UserPayment
        fields = ('__all__')

class PaymentRefundSerializer(serializers.Serializer):
    user_payment_id = serializers.IntegerField(validators=[
                                                UniqueValidator(
                                                    queryset=PaymentRefund.objects.all()
                                                )
                                            ])

    def create(self, validated_data):
        return PaymentRefund.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_payment_id = validated_data.get(
                                                    'user_payment_id',
                                                    instance.user_payment_id
                                                    )
        instance.save()
        return instance

    class Meta:
        model = PaymentRefund
        fields = ('__all__')

class CompanyPaymentSerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    price = serializers.FloatField()
    origin_account = serializers.CharField(max_length = 30)
    destination_account = serializers.CharField(max_length = 30)

    def create(self, validated_data):
        return CompanyPayment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.company_id = validated_data.get('company_id', instance.company_id)
        instance.price = validated_data.get('price', instance.price)
        instance.origin_account = validated_data.get(
                                                    'origin_account',
                                                    instance.origin_account
                                                    )
        instance.destination_account = validated_data.get(
                                                    'destination_account',
                                                    instance.destination_account
                                                    )

        instance.save()
        return instance

    class Meta:
        model = CompanyPayment
        fields = ('__all__')