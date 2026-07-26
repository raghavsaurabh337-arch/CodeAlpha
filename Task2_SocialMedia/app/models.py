from django.db import models
from django.contrib.auth.models import User


# User Profile
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="profile/",
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    followers = models.ManyToManyField(
        User,
        related_name="following",
        blank=True
    )


    def followers_count(self):
        return self.followers.count()


    def following_count(self):
        return self.user.following.count()


    def __str__(self):
        return self.user.username



# Post Model
class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="posts/",
        blank=True
    )

    caption = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    likes = models.ManyToManyField(
        User,
        related_name="likes",
        blank=True
    )


    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.user.username



# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.comment