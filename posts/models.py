from django.db import models
from users.models import MyUser

class Posts(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.TextField(verbose_name='What you are thinking')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.post

    class Meta:
        db_table = 'Posts'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
