from django.db import models

'''
w plikach statycznych mam obrazki
użytkownik może ściągnąć do siebie na komputer obrazek
użytkownikowi w profilu powinna się wyświetlać lista obrazków, które ściągnął (tylko nazwy, bez linków)

1. robię użytkownika - logowanie, 
                        wylogowywanie, 
                        lista użytkowników (permissions is supereuser)
                        widok pojedycznego użytkownika (tylko własne konto or is superuser)

2. plan musi być osobnym modelem i modelchoicefield - admin musi móc dodawać customowe
'''

def pics_dir_path(filename):
    return 'pics/{1}'.format(filename)

class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=pics_dir_path)
    


