from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Each class is it's own table in the DB.
# Each attibute of each class is its' own
# field in the DB

# "Post" is a table in the DB..
class Post(models.Model):
    # DB field called "title"
    title = models.CharField(max_length=100) #title is a field of the db
    # DB field called "content"
    content = models.TextField()
    # We are just passing the actual timezone function as the default value, but we are not executing the function yet.
    # DB field called "date_posted"
    date_posted = models.DateTimeField(default=timezone.now)
    # Need an author for each post.
    # User is a separate table
    # We need to import the djang user model above
    # from django.contrib.auth.models import User
    # Post model and User model will have 1 to many relationship.
    # 1 user can have multiple posts, but a post can only have 1 author(user)
    # We can create this relationship by using a foreignkey.
    # Can use models.ForeignKey to create this relationship.
    # Remember, below "User" is a table, so we are creating a foreign key
    # on the User table.
    # DB field called "author", that has a foreignkey on it ? that
    # points to the "User" table.
    # on_delete is telling django what to do if the user created the post
    # but gets deleted.
    # on_delete=models.CASCADE tells django that if a user is deleted,
    # we want to delete their post as well.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # dunder str method, double underscore
    def __str__(self):
        return self.title
