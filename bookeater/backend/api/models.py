from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator



class User(AbstractUser):
    STATUS_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
    )
    readlist = models.ManyToManyField('Book', related_name='users', blank=True)
    age = models.IntegerField(blank=True, default=0)
    sex = models.CharField(blank=True, max_length=1, choices=STATUS_CHOICES)
    public_score = models.BooleanField(default=True)
    is_author = models.BooleanField(default=False)
    token = models.CharField(blank=True, max_length=32)



class Author(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    full_name = models.CharField(max_length=128)
    description = models.TextField(max_length=1028, )
    content = models.TextField()
    related_category = models.ManyToManyField('Category', related_name='authors', blank=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    thumbnail = models.ImageField(upload_to='media/authors', null=False, blank=False)
    image = models.ImageField(upload_to='media/authors', null=False, blank=False)
    popular_author = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    written_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.full_name



class Quote(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    author = models.CharField(max_length=128)
    thumbnail = models.ImageField(upload_to='media/quotes', null=False, blank=False)
    description = models.TextField(max_length=512, )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    written_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.description[:35]



class Category(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1028)
    content = models.TextField()
    related_author = models.ManyToManyField(Author, related_name='categories', blank=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    thumbnail = models.ImageField(upload_to='media/categories', null=False, blank=False)
    image = models.ImageField(upload_to='media/categories', null=False, blank=False)
    popular_category = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    written_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title



class Book(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    title =  models.CharField(max_length=128)
    category =  models.ManyToManyField(Category, related_name="books")
    author =  models.ManyToManyField(Author, related_name="books")
    slug = models.SlugField(null=False, blank=False, unique=True)
    description =  models.TextField(max_length=512, )
    content =  models.TextField()
    thumbnail =  models.ImageField(upload_to='media/books', null=True, blank=True)
    image =  models.ImageField(upload_to='media/books', null=True, blank=True)
    score =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, validators=[MinValueValidator(0),MaxValueValidator(10)], default=0)
    rates = models.IntegerField(blank=True, default=0)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    written_by = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class News(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    content = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='media/news', null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    written_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title



class Reviewed_Book(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    title = models.CharField(max_length=128)
    author =  models.ManyToManyField(Author, related_name="reviewed_books")
    category =  models.ManyToManyField(Category, related_name="reviewed_books")
    description = models.TextField(max_length=1028)
    content = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    critic = models.ForeignKey(User, related_name="reviewed_books", on_delete=models.CASCADE)
    thumbnail =  models.ImageField(upload_to='media/reviewed_books', null=False, blank=False)
    image =  models.ImageField(upload_to='media/reviewed_books', null=False, blank=False)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    written_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title



class ContactUs(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=512, )
    content = models.TextField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.subject



class Score(models.Model):
    user = models.ForeignKey(User, related_name="scores", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='scores', on_delete=models.CASCADE)
    user_score = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])

    def __str__(self):
        return self.user.username



class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    reply_to = models.ForeignKey('Comment', related_name="comments", blank=True, null=True, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dis_like = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)



class Like(models.Model):
    STATUS_CHOICES = (
        ('l', 'like'),
        ('d', 'dislike'),
    )
    user = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="likes", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
