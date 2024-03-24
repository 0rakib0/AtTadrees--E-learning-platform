from ast import Str
import json
import requests
from . import _constants as const



def __init__(self, isSandbox=True, storeID=const.storeID, successUrl=const.succesUrl, failUrl=const.failUrl, cancelUrl=const.cancelUrl, transactionID='testTrId', transactionAmount='100', signature=const.signature, description='Description', customerName='Test user', customerEmail='sandbox@email.com', customerMobile='0111111111', customerAddress1='', customerAddress2='', customerCity='', customerState='', customerPostCode='') -> None:
        self.isSandbox = isSandbox
        self.storeID = storeID
        self.successUrl = successUrl
        self.failUrl = failUrl
        self.cancelUrl = cancelUrl
        self.transactionID = transactionID
        self.transactionAmount = transactionAmount
        self.signature = signature
        self.description = description
        self.customerName = customerName
        self.customerEmail = customerEmail
        self.customerMobile = customerMobile
        self.customerAddress1 = customerAddress1
        self.customerAddress2 = customerAddress2
        self.customerCity = customerCity
        self.customerState = customerState
        self.customerPostCode = customerPostCode










# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.conf import settings
# from aamarpay import PaymentRequest

# from .forms import PaymentForm #create paymentform 

# def payment_view(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             amount = form.cleaned_data['amount']
#             customer_name = form.cleaned_data['customer_name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']

#             payment_request = PaymentRequest(
#                 store_id=settings.AAMARPAY_SETTINGS['store_id'],
#                 signature_key=settings.AAMARPAY_SETTINGS['signature_key'],
#                 sandbox_mode=settings.AAMARPAY_SETTINGS['sandbox_mode']
#             )
#             payment_request.set_transaction_details(
#                 amount=str(amount),
#                 currency='BDT',
#                 transaction_id='YOUR_UNIQUE_TRANSACTION_ID',
#                 success_url=request.build_absolute_uri(reverse('payment_success')),
#                 fail_url=request.build_absolute_uri(reverse('payment_fail')),
#                 cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
#                 ipn_url=request.build_absolute_uri(reverse('payment_ipn')),
#             )
#             payment_request.set_customer_info(
#                 name=customer_name,
#                 email=email,
#                 phone=phone,
#                 address='N/A',
#                 city='N/A',
#                 state='N/A',
#                 postcode='N/A',
#                 country='Bangladesh',
#             )
#             payment_url = payment_request.create_payment()

#             return redirect(payment_url)
#     else:
#         form = PaymentForm()

#     return render(request, 'payment.html', {'form': form})