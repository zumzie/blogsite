from django.db import models
from django.contrib.auth.models import User  # Default Django user model
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ArticlePost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE, default=1)
    image = models.ImageField(db_column='img_url', upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])])

    def clean(self):
        if self.image:
            try:
                img = Image.open(self.image)
                img.verify()  # Verify if it's a valid image
            except (IOError, SyntaxError) as e:
                raise ValidationError("The file is not a valid image.")

class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, related_name='comments', on_delete=models.CASCADE, default=1)
    author = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image_data = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=255)

    def __str__(self):
        return self.image_name
    
'''
class Category(models.Model):
    class Meta:
        db_table = 'categories'

    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    class Meta:
        db_table = 'articles'

    article_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE, default=1)
    image = models.ImageField(db_column='img_url', upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])])

    def clean(self):
        if self.image:
            try:
                img = Image.open(self.image)
                img.verify()  # Verify if it's a valid image
            except (IOError, SyntaxError) as e:
                raise ValidationError("The file is not a valid image.")

class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    comment_id = models.AutoField(primary_key=True)
    article_id = models.ForeignKey(Article, related_name='articles', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
class Image(models.Model):
    class Meta:
        db_table = 'images'

    image_id = models.AutoField(primary_key=True)
    image_data = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=255)

    def __str__(self):
        return self.image_name
'''