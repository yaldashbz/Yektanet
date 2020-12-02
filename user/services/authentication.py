from rest_framework.authtoken.models import Token

from user.models.customer import Customer


def get_or_create_token(customer: Customer):
    token = Token.objects.filter(user=customer).first()
    if token is not None:
        return token

    token = Token.objects.create(user=customer)
    return token
