from django.db import models

class SettingsLoader(models.Model):
    max_comment_length = models.IntegerField(default=500)
    opacity = models.FloatField(default=0.5)
    theme = models.CharField(max_length=10)
    times_to_run = models.IntegerField(default=0)
    reddit_client_id = models.CharField(max_length=22)
    reddit_password = models.CharField(max_length=40)
    post_id = models.CharField(max_length=9)
    ttschoice = models.CharField(max_length=12)
    aws_voice = models.CharField(max_length=12)
    reddit_username = models.CharField(max_length=30)
    reddit_client_secret = models.CharField(max_length=30)
    streamlabs_voice = models.CharField(max_length=12)
    subreddit = models.CharField(max_length=30)
    postlang = models.CharField(max_length=2)
    allow_nsfw = models.BooleanField(default=False)
    reddit_2fa = models.CharField(max_length=3)
    

