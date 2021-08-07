import requests

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse
from django.template.loader import get_template
from django.urls import reverse

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import ScheduleCallSerializer
from keel.authentication.backends import JWTAuthentication
from keel.authentication.models import User
from keel.calendly.utils import calendly_business_logic
from keel.calendly.constants import CALENDLY_WEBHOOK_PATH
from keel.call_schedule.models import CallSchedule
from keel.calendly.models import CalendlyCallSchedule

import logging
logger = logging.getLogger('app-logger')


class ScheduleCallViewSet(GenericViewSet):

    def get_schedule_page(self, request, **kwargs):
        template = get_template('calendly_landing.html')  # getting our templates
        return HttpResponse(template.render())


class RCICScheduleUrl(GenericViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_call_schedule_url(self, request, **kwargs):
        response = {
            'status': 1,
            "message": ''
        }
        try:
            user = request.user
            rcic_obj = user.users_cases.get(is_active=True).agent
        except ObjectDoesNotExist as err:
            response["status"] = 0
            response["message"] = "Case does not exist for the user"
            return Response(response, status.HTTP_400_BAD_REQUEST)
        except MultipleObjectsReturned as err:
            response["status"] = 0
            response["message"] = "Multiple RCIC assigned to the user"
            return Response(response, status.HTTP_400_BAD_REQUEST)
        schedule_url = calendly_business_logic.get_agent_schedule_url(user, rcic_obj)

        if not schedule_url:
            response["status"] = 0
            response["message"] = "Error getting schedule url of assigned RCIC"
            return Response(response, status.HTTP_400_BAD_REQUEST)

        response["message"] = {"schedule_url": schedule_url}
        return Response(response, status=status.HTTP_200_OK)


class CallScheduleViewSet(GenericViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def create_call_schedule(self, request, **kwargs):
        response = {
            "status": 1,
            "message": ""
        }
        serializer = ScheduleCallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        try:
            host_user = request.user.users_cases.get(is_active=True).agent
        except Exception as err:
            response["status"] = 0
            response["message"] = "User not connected to any agent"
            return Response(response, status.HTTP_400_BAD_REQUEST)

        event_details = calendly_business_logic.create_event_schedule(
            request.user, host_user, validated_data["calendly_invitee_url"])

        if not event_details["status"]:
            response["status"] = 0
            response["message"] = "Error while creating schedule Id"
            return Response(response, status.HTTP_500_INTERNAL_SERVER_ERROR)

        response["message"] = event_details["data"]

        return Response(response, status.HTTP_200_OK)

    def reschedule_call(self, request, **kwargs):
        response = {
            "status": 0,
            "message": ""
        }
        schedule_id = kwargs["schedule_id"]

        try:
            schedule_obj = CallSchedule.objects.get(
                visitor_user=request.user, pk=schedule_id, is_active=True,
                status__in=(CallSchedule.ACTIVE, CallSchedule.RESCHEDULED))
        except ObjectDoesNotExist as err:
            response["message"] = "Error getting schedule with this id and associated user which is in" \
                                  "active or rescheduled status"
            return Response(response, status.HTTP_500_INTERNAL_SERVER_ERROR)

        reschedule_details = calendly_business_logic.cancel_reschedule_scheduled_event(schedule_obj)
        if not reschedule_details["status"]:
            response["message"] = reschedule_details["error"]
            return Response(response, status.HTTP_500_INTERNAL_SERVER_ERROR)

        response["status"] = 1
        response["message"] = "Reschedule successful"

        return Response(response, status.HTTP_200_OK)

    def cancel_scheduled_call(self, request, **kwargs):
        response = {
            "status": 0,
            "message": ""
        }
        schedule_id = kwargs["schedule_id"]
        try:
            schedule_obj = CallSchedule.objects.get(
                visitor_user=request.user, pk=schedule_id, is_active=True,
                status__in=(CallSchedule.ACTIVE, CallSchedule.RESCHEDULED))
        except ObjectDoesNotExist as err:
            response["message"] = "Error getting schedule with this id and associated user which is in" \
                                      "active or rescheduled status"
            return Response(response, status.HTTP_500_INTERNAL_SERVER_ERROR)
        calendly_business_logic.cancel_reschedule_scheduled_event(schedule_obj)

        return Response(response, status.HTTP_200_OK)

    def get_scheduled_call(self, request, **kwargs):
        response = {
            "status": 0,
            "message": ""
        }
        try:
            call_schedule_objs = CallSchedule.objects.filter(
                visitor_user=request.user, is_active=True,
                status__in=(CallSchedule.ACTIVE, CallSchedule.RESCHEDULED))
        except ObjectDoesNotExist:
            response["message"] = "No Active schedule for user exists"
            return Response(response, status.HTTP_400_BAD_REQUEST)

        if not call_schedule_objs:
            response["message"] = "No Active schedule for user exists"
            return Response(response, status.HTTP_200_OK)

        scheduled_event_details = calendly_business_logic.get_scheduled_event_details(call_schedule_objs)

        if not scheduled_event_details["status"]:
            response["message"] = scheduled_event_details["error"]
            return Response(response, status.HTTP_500_INTERNAL_SERVER_ERROR)

        response["status"] = 1
        response["message"] = scheduled_event_details["data"]
        return Response(response, status.HTTP_200_OK)


class WebHookViewSets(GenericViewSet):

    def subscribe(self, request, **kwargs):
        response = {
            "status": 0,
            "message": ""
        }
        if not request.user.is_superuser:
            return Response("User is not a superuser", status.HTTP_400_BAD_REQUEST)
        url = settings.CALENDLY_BASE_URL + CALENDLY_WEBHOOK_PATH
        payload = {
            "url": reverse("calendly_webhook_process_events"),
            "events": settings.CALENDLY_WEBHOOK_EVENTS,
            "organization": settings.CALENDLY_ORGANIZATION_URL,
            "scope": settings.CALENDLY_WEBHOOK_SCOPE,
            "signing_key": settings.CALENDLY_SIGNING_KEY
        }
        headers = {
            "authorization": "Bearer " + settings.CALENDLY_PERSONAL_TOKEN
        }
        request_resp = requests.post(url=url, headers=headers, payload=payload)
        status_code = request_resp.status_code
        if status_code == status.HTTP_201_CREATED:
            response["status"] = 1
            response["message"] = "Webhook created successfully"
            return Response(response, status.HTTP_200_OK)
        else:
            response["message"] = "Error creating webhook with status code - {}".format(status_code)
            return Response(response, status_code)

    def process_events(self, request, **kwargs):

        pass