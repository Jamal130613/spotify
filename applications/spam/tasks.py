import time
from django.core.mail import send_mail
from applications.spam.models import Contact
from spotify.celery import app


@app.task
def spam_email():
    full_link = f'Hi! We are very happy that you are listening to music in our app!'
    for i in Contact.objects.all():
        send_mail(
            'Spotify',
            full_link,
            'jamalaskarovaa@gmail.com',
            [i.email]
        )
