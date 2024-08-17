from django.db import models
import uuid

# Create your models here.
class Users(model.Model):
    username = models.CharField(max_length=255)
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Chat(model.Model):
    chat_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(Users, on_delete=models.SET_NULL)
    user2 = models.ForeignKey(Users, on_delete=models.SET_NULL)

# class GroupChat(model.Model): #This is to implement group chat later
l;
