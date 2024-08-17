from rest_framework import serializers
from django.contrib.auth.models import Group, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [username, tag, created]

class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coonnection
        fields = [con_id, user1, user2, created]


    
