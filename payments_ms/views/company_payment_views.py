from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from ..models import CompanyPayment
from ..serializers import CompanyPaymentSerializer

class CompanyPaymentView(APIView):
    def get(self, request):
        payments = CompanyPayment.objects.all()
        payments = list(payments.values())
        return Response({"Companies payments": payments})
    
    def post(self, request):
        payment = request.data.get('company_payment')

        serializer = CompanyPaymentSerializer(data=payment)
        if serializer.is_valid(raise_exception=True):
            payment_saved = serializer.save()
        return Response({"Company payment creation": "success"})

    def put(self, request, pk):
        payment = get_object_or_404(CompanyPayment.objects.all(), pk=pk)
        data = request.data.get('company_payment')
    
        serializer = CompanyPaymentSerializer(instance=payment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            payment_saved = serializer.save()
        return Response({"Company payment updated": "success"})

    def delete(self, request, pk):
        payment = get_object_or_404(CompanyPayment.objects.all(), pk=pk)
        payment.delete()
        return Response({"Company payment deleted": "success"})
    

