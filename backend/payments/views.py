# import stripe
# from django.conf import settings
# from django.views import View
# from models import Product
# from flask import Flask, redirect, request
#
# stripe.api_key = settings.STRIPE_SECREY_KEY
#
#
# class CreateCheckoutSessionView(View):
#     def product_detail(self, request, product_id):
#         product = Product.objects.get(pk=product_id)
#         context = {
#             'product': product,
#             'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
#         }