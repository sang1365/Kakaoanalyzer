from django.db import models
from django.db.models import ForeignKey


class chat_title(models.Model):
    title = models.CharField(max_length=20)
    update_date = models.DateTimeField()

    def __int__(self):
        return self.id


class chat_data(models.Model):
    idx = models.IntegerField()
    speaker = models.CharField(max_length=20)
    chat = models.TextField()
    timestamp = models.DateTimeField()
    chat_title_id = ForeignKey(chat_title, on_delete=models.CASCADE)
    emoji_cnt = models.IntegerField()
    insert_time = models.DateTimeField()

    def __int__(self):
        return self.chat_title_id
