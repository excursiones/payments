from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from ..models import UserPayment
from ..serializers import UserPaymentSerializer

class UserPaymentView(APIView):
    def get(self, request):
        payments = UserPayment.objects.all()
        payments = list(payments.values())
        return Response({"Users payments": payments})
    
    def post(self, request):
        payment = request.data.get('user_payment')

        serializer = UserPaymentSerializer(data=payment)
        if serializer.is_valid(raise_exception=True):
            payment_saved = serializer.save()
        return Response({"User payment creation": "success"})

    def put(self, request, pk):
        payment = get_object_or_404(UserPayment.objects.all(), pk=pk)
        data = request.data.get('user_payment')
    
        serializer = UserPaymentSerializer(instance=payment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            payment_saved = serializer.save()
        return Response({"User payment updated": "success"})

    def delete(self, request, pk):
        payment = get_object_or_404(UserPayment.objects.all(), pk=pk)
        payment.delete()
        return Response({"User payment deleted": "success"})
    

