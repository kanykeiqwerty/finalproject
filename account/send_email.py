from django.core.mail import send_mail
from recipe.models import Post

def send_confirmation_email(user):
    code=user.activation_code
    full_link=f'http://localhost:8000/api/v1/account/activate/{code}/'
    to_email=user.email
    send_mail('Здравствуйту. активируйте ваш аккаунт',
    f'что-бы активироватьваш аккаунт, нужно перейти по ссылке:{full_link}', 
    'ghjvgyjvgyj@gmail.com', 
    [to_email,],
    fail_silently=False)


def send_reset_password(user):
    code=user.activation_code
    to_email=user.email
    send_mail(
        'Subject', 
        f'yout code for reset password:{code}',
        'from@example.com', 
        [to_email,],
        fail_silently=False
    )


def send_html_email():
    from django.template.loader import render_to_string
    post =Post.objects.all()[0]
    html_message=render_to_string('f.html', {'name':post.title, 'desc':post.description})
    send_mail(
        'Subject', 
        'letter', 
        'example@admin.com', 
        ['ghjvgyjvgyj@gmail.com'], 
        html_message=html_message, 
        fail_silently=False
    )