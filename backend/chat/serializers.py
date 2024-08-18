from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Networks



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
    
        
class NetworksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Networks
        fields = ['con_id', 'user1', 'user2', 'created']


    
