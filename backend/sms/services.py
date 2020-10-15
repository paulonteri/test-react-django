import africastalking

# Initialize SDK
username = "sandbox"
api_key = "d4f152e77e8153946601d8b6aecc6c2ca1fbf5a06d7f68adacf5c840e5061f52"
africastalking.initialize(username, api_key)

# Initialize SMS
sms = africastalking.SMS


def send_sms(recipients, message):
    recipients = recipients
    message = message
    # Set your shortCode or senderId
    # sender = "shortCode or senderId"

    try:
        response = sms.send(message, recipients)
        print(response)
    except Exception as e:
        print('Encountered an error while sending: %s' % str(e))
        print(e)


def send_single_sms():
    recipients = ["+254703103580"]
    message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
    send_sms(recipients=recipients, message=message)
