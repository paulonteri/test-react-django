from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from celery.decorators import task

from .services import activate_account_mail


@task(name="sum_two_numbers")
def add(x, y):
    return x + y


class SendMail(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        # activate_account_mail()
        return Response(add.delay(7, 8))
