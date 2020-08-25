""" function that creates a random string for a random url"""

#Utilities Django
import random, string

#model
from .models import SetUrl

def random_url_gen():
    
    create = False
    
    while not create:
        random_url_gen = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
        
        #Check if already exists the shor url generated
        already_exists = SetUrl.objects.filter(short_url__contains=random_url_gen)
        
        if already_exists:
            return 'si__existe'
        
        else:
            return random_url_gen