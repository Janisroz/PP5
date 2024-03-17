from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from coaching.models import Session

# Create your models here.
class Post(models.Model):
    """
    Model for Session Posts
    """
    session = models.ForeignKey(Session, on_delete=models.CASCADE,
                                 related_name="session_posts")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="session_posts"
    )
    description = models.TextField()
    session_rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0,
    )
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-post_date"]
