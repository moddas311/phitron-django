from django.db import models
from categories.models import  Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # ekta post multiple categoryr moddhe thakte 
    # pare abar categoryr moddhe multiple post thakte pare 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'posts/media/uploads/', blank = True, null = True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length = 400)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True) # post time rekhe dibe
    
    def __str__(self) -> str:
        return f'Comments by {self.name}'
    