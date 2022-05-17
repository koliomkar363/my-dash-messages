from django.db import models
from django.contrib.auth.models import User


class UserMessage(models.Model):
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usermessages"
    )

    def __str__(self):
        return f"{self.created_by.username}'s message"
