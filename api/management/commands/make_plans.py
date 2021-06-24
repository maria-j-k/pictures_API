from django.core.management.base import BaseCommand 

from users.models import Plan, ThumbSize

class Command(BaseCommand): 
    help = 'Create default plans'

    def handle(self, *args, **kwargs):
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
        
        self.stdout.write(f'ThumbSizes created: {small}, {big}')
        self.stdout.write(f'Plans created: {basic}, {premium}, {enterprise}')

