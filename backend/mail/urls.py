from django.urls import path

from mail.api import SendMail

urlpatterns = [
    path('api/v2.0/mail/send', SendMail.as_view(), name='Get All Exam results'),

]
