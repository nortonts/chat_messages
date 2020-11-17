from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

 
 
class Chat_message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-timestamp",)