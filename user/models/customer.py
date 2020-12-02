from django.db.models import BigIntegerField
from django.contrib.auth.models import User


class Customer(User):

    balance = BigIntegerField(
        verbose_name='موجودی',
        default=0
    )

    def __str__(self):
        return self.username + ' : ' + str(self.balance)

