import time
from django.core.mail import send_mail
from spotify.celery import app


@app.task
def celery_send_confirmation_email(code, email):
    time.sleep(10)
    full_link = f'http://localhost:8000/account/active/{code}'
    send_mail(
        'Spotify',
        full_link,
        'jamalaskarovaa@gmail.com',
        [email]
    )

@app.task
def celery_forgot_password_email(code, email):
    time.sleep(10)
    send_mail(
            'Password reset',
            f'Your activation code: {code}',
            'jamalaskarovaa@gmail.com',
            [email]
        )