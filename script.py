from api.models import *
from users.models import *




def populate():
    small = ThumbSize.objects.create(name='small', size=200)
    big = ThumbSize.objects.create(name='big', size=400)
    basic = Plan.objects.create(
            name='Basic',
            original=False,
            expiring_links=True
            )
    basic.thumbsizes.add(small)
    basic.save()
    premium = Plan.objects.create(
            name='Premium',
            original=True,
            expiring_links=True
            )
    premium.thumbsizes.add(small)
    premium.thumbsizes.add(big)
    premium.save()
    enterprise = Plan.objects.create(
            name='Enterprise',
            original=True,
            expiring_links=True
            )
    enterprise.thumbsizes.add(small)
    enterprise.thumbsizes.add(big)
    enterprise.save()

    users = [('basic@demo.pl', basic), ('premium@demo.pl', premium), ('enterprise@demo.pl', enterprise)]
    password = 'testpass'

    for user in users:
        User.objects.create_user(email=user[0], password=password, plan=user[1])
