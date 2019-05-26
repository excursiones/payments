from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from ..models import PaymentRefund, UserPayment
from ..serializers import PaymentRefundSerializer

class PaymentRefundView(APIView):
    def get(self, request):
        refunds = PaymentRefund.objects.all()
        refunds = list(refunds.values())
        return Response({"Payment refunds": refunds})
    
    def post(self, request):
        data = request.data.get('payment_refund')
        user_payment = get_object_or_404(UserPayment.objects.all(),
                                        id=data['user_payment_id']
                                        )

        serializer = PaymentRefundSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            refund_saved = serializer.save()
        return Response({"Payment refund creation": "success"})

    def put(self, request, pk):
        refund = get_object_or_404(PaymentRefund.objects.all(), pk=pk)
        data = request.data.get('payment_refund')
        user_payment = get_object_or_404(UserPayment.objects.all(),
                                        id=data['user_payment_id']
                                        )

        serializer = PaymentRefundSerializer(instance=refund, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            payment_saved = serializer.save()
        return Response({"Payment refund updated": "success"})

    def delete(self, request, pk):
        refund = get_object_or_404(PaymentRefund.objects.all(), pk=pk)
        refund.delete()
        return Response({"Payment refund deleted": "success"})