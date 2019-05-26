from django.urls import path

from .views import *


app_name = "payments_ms"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('user_payments/', UserPaymentView.as_view()),
    path('user_payments/<int:pk>', UserPaymentView.as_view()),
    path('company_payments/', CompanyPaymentView.as_view()),
    path('company_payments/<int:pk>', CompanyPaymentView.as_view()),
    path('payment_refunds/', PaymentRefundView.as_view()),
    path('payment_refunds/<int:pk>', PaymentRefundView.as_view()),
]