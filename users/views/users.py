from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from users.serializers.users import *
from users.models import *


class UserDetailView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(data=request.data, instance=user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UserCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(id=serializer.data.get('id'))
        plan = SubscriptionPlan.objects.create(user=user, plan=SubscriptionPlan.FREE)
        return Response({}, status=status.HTTP_201_CREATED)


class PresentMoneyDetailView(APIView):
    def get(self, request, transaction_id):
        transaction = get_object_or_404(MoneyForPresent, id=transaction_id)
        serializer = MoneyPresentSerializer(transaction)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, transaction_id):
        transaction = get_object_or_404(MoneyForPresent, id=transaction_id)
        serializer = MoneyPresentSerializer(data=request.data, instance=transaction, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class PresentMoneyCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = MoneyPresentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)


class PresentBadgeDetailView(APIView):
    def get(self, request, badge_id):
        badge = get_object_or_404(BadgeForPresent, id=badge_id)
        serializer = BadgePresentSerializer(badge)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, badge_id):
        badge = get_object_or_404(BadgeForPresent, id=badge_id)
        serializer = BadgePresentSerializer(data=request.data, instance=badge, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class PresentBadgeCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = BadgePresentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)


class PresentVerificationDetailView(APIView):
    def get(self, request, verification_label_id):
        verification_label = get_object_or_404(VerificationLabelForPresent, id=verification_label_id)
        serializer = VerificationPresentSerializer(verification_label)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, verification_label_id):
        verification_label = get_object_or_404(VerificationLabelForPresent, id=verification_label_id)
        serializer = VerificationPresentSerializer(data=request.data, instance=verification_label, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class PresentVerificationCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = VerificationPresentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)


class PresentSubscriptionPlanDetailView(APIView):
    def get(self, request, sub_plan_id):
        subscription_plan = get_object_or_404(SubscriptionPlanForPresent, id=sub_plan_id)
        serializer = SubscriptionPlanPresentSerializer(subscription_plan)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, sub_plan_id):
        subscription_plan = get_object_or_404(SubscriptionPlanForPresent, id=sub_plan_id)
        serializer = SubscriptionPlanPresentSerializer(data=request.data, instance=subscription_plan, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class PresentSubscriptionPlanCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = SubscriptionPlanPresentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)
