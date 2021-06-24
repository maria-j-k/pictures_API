from django.core.management.base import BaseCommand 

from users.models import Plan, User

class Command(BaseCommand): 
    help = 'Create demo users'

    def handle(self, *args, **kwargs):
        basic = Plan.objects.get(name='Basic')
        premium = Plan.objects.get(name='Premium')
        enterprise = Plan.objects.get(name='Enterprise')
        users = [('basic@demo.pl', basic), 
                ('premium@demo.pl', premium), 
                ('enterprise@demo.pl', enterprise)]
        password = 'testpass'

        for user in users:
            User.objects.create_user(email=user[0], password=password, plan=user[1])


        
            self.stdout.write(f'User created: plan: {user[1]}, email: {user[0]}, password: {password}')

