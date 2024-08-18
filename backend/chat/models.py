from django.db import models
import uuid
from django.contrib.auth.models import User


class Networks(models.Model):
    con_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='A')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='B')
    created = models.DateTimeField(auto_now_add=True)


class Messages(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    connection = models.ForeignKey(Networks, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)



    
# class GroupChat(model.Model): #This is to implement group chat later
