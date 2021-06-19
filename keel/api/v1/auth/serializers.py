from rest_framework import serializers
from keel.authentication.models import (User, UserDocument)
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from keel.api.v1 import utils as v1_utils
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q
# from keel.common import models as common_models
import logging
logger = logging.getLogger('app-logger')


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class OTPSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField(min_value=5000000000,max_value=9999999999)
    via_sms = serializers.BooleanField(default=True, required=False)
    via_whatsapp = serializers.BooleanField(default=False, required=False)
    request_source = serializers.CharField(required=False, max_length=200)

    def validate(self, attrs):
        # otp_obj = OtpVerifications.objects.filter(phone_number=attrs.get('phone_number')).order_by('-id').first()
        # if not attrs.get('via_whatsapp') and otp_obj and not otp_obj.is_expired and (
        #         datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE)) - v1_utils.aware_time_zone(
        #         otp_obj.updated_at)).total_seconds() < OtpVerifications.TIME_BETWEEN_CONSECUTIVE_REQUESTS:
        #     raise serializers.ValidationError('Please try again in a moment.')
        # if otp_obj:
        #     attrs['otp_obj'] = otp_obj
        return attrs


class UserDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDocument
        fields = ('id', 'doc','user')


    def create(self, validated_data):

        user_doc = UserDocument.objects.create(**validated_data)
        return user_doc




