from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_my_mail(email_subject, message, recipients, bcc, reply_to, sender):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    email_subject = email_subject
    message = message
    recipients = recipients
    bcc = bcc
    reply_to = reply_to
    sender = sender
    email = EmailMessage(
        email_subject,
        message,
        sender,
        recipients,
        bcc,
        reply_to=reply_to,
        headers={'Message-ID': 'foo'},
    )
    email.content_subtype = "html"
    email.send()


# TODO: Find way to get current site and store it
# from django.contrib.sites.shortcuts import get_current_site
# def send_mail(request):
# current_site = get_current_site(request)

def activate_account_mail():
    email_subject = "Activate Your Account"
    recipients = ["onteripaul@gmail.com"]
    bcc = ["onteripaul@outlook.com", "paulonteri@gmail.com"]
    reply_to = ['paulonteri@outlook.com']
    sender = "paulonteri@gmail.com"
    #
    recipient_name = "Paul Onteri"
    message = render_to_string("mails/accounts/activate.html", ({
        "user": recipient_name,
        # "domain": current_site.domain,
        "domain": "https://www.linkedin.com/in/paulonteri/",
    }))
    # #
    send_my_mail.delay(email_subject=email_subject, message=message, recipients=recipients, bcc=bcc, reply_to=reply_to,
                       sender=sender)


from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
def some_task():
    print("Cron")
    # do something

some_task()
