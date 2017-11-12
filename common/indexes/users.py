from authorization.models import User
from profiles.index import UserIndex
from elasticsearch_dsl import Index

def rebuild_index():
    """ Rebuild index for the users """
    
    Index('users').delete()
    UserIndex.init()
    users = User.objects.prefetch_related('companies', 'attachments')
    for user in users:
        print(UserIndex.store_index(user))
