from django.contrib.auth.models import User
from django.db import models

class UserAccount(models.Model):
	user = models.ForeignKey(User)
	account = models.CharField(max_length=200)
	account_id = models.CharField(max_length=100)
	access_token = models.CharField(max_length=4000)
	date_created = models.IntegerField()
	account_data = models.TextField(null=True)
	account_pic = models.URLField(null=True)
	account_handle = models.CharField(max_length=200, null=True)
	
	def __unicode__(self):
		return self.account

class Square(models.Model):
	user = models.ForeignKey(User)
	content_src = models.CharField(max_length=200)
	content_type = models.CharField(max_length=50)
	content_data = models.CharField(max_length=4000)
	content_description = models.CharField(max_length=4000,null=True)
	date_created = models.IntegerField('date published',null=True)
	shared_count = models.IntegerField(null=True)
	liked_count = models.IntegerField(null=True)
	#square_type = models.CharField(max_length=50, null=True)
	user_account = models.ForeignKey(UserAccount, null=True)

	def __unicode__(self):
		return self.content_data

class UserSquare(models.Model):
	user = models.ForeignKey(User)
	square = models.ForeignKey(Square)
	date_shared = models.IntegerField('date shared')

	def __unicode__(self):
		return self.date_shared
class RequestInvitation(models.Model):
	email = models.EmailField(max_length=254)
	date_requested = models.IntegerField('date requested')
	
	def __unicode__(self):
		return self.email

class Emailer(models.Model):
	to = models.EmailField(max_length=254,null=False)
	from_email = models.EmailField(max_length=254, null=False)
	body = models.TextField()
	subject = models.CharField(max_length=100)
	date_created = models.IntegerField()
	is_sent = models.BooleanField(default=False)
	status = models.TextField(null=True)

class Relationship(models.Model):
	subscriber = models.ForeignKey(User,related_name='subscriber')
	producer = models.ForeignKey(User, related_name='producer')
	date_subscribed = models.IntegerField('date subscribed')
	permission = models.BooleanField()

class SyncTwitterFeed(models.Model):
	last_tweet = models.CharField(max_length=40)
	date_created = models.IntegerField()
	last_sync_time = models.IntegerField()
	def __unicode__(self):
		return self.last_tweet