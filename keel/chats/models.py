from django.db import models

from keel.Core.models import TimeStampedModel, SoftDeleteModel
from keel.cases.models import Case
from keel.authentication.models import User

# Create your models here.

class ChatRoom(TimeStampedModel, SoftDeleteModel):

    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name='users_chatrooms')
    agent = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name='agents_chatrooms')
    case = models.ForeignKey(Case,on_delete=models.deletion.DO_NOTHING, related_name='cases_chatrooms') 


class Chat(TimeStampedModel, SoftDeleteModel):

    sender = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING, related_name='sender_chats')
    message = models.TextField(null=True, blank=True)
    chatroom = models.ForeignKey(ChatRoom,on_delete=models.deletion.DO_NOTHING, related_name='chatroom_chats') 


