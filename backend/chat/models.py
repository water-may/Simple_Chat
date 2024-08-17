from django.db import models
import uuid




class Users(models.Model):
    """
    For each user, `username`= any,, `user_id` = any, `created` = date of registration
    """
    username = models.CharField(max_length=255)
    tag = models.IntegerField(unique=True)
    user_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    password = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Connection(models.Model):
    con_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user1 = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='A')
    user2 = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='B')
    created = models.DateTimeField(auto_now_add=True)


class Messages(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)



    
# class GroupChat(model.Model): #This is to implement group chat later
