# Generated by Django 3.2 on 2022-08-13 10:34

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.IntegerField(blank=True, default=0)),
                ('sex', models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('public_score', models.BooleanField(default=True)),
                ('is_author', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=32)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1028)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(upload_to='media/authors')),
                ('image', models.ImageField(upload_to='media/authors')),
                ('popular_author', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=512)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='media/books')),
                ('image', models.ImageField(upload_to='media/books')),
                ('score', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('rates', models.IntegerField(blank=True, default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1)),
                ('author', models.ManyToManyField(related_name='books', to='api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1028)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(upload_to='media/categories')),
                ('image', models.ImageField(upload_to='media/categories')),
                ('popular_category', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1)),
                ('related_author', models.ManyToManyField(blank=True, related_name='categories', to='api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('like', models.IntegerField(default=0)),
                ('dis_like', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.book')),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=512)),
                ('content', models.TextField()),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=512)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='media/news')),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('thumbnail', models.ImageField(upload_to='media/quotes')),
                ('description', models.TextField(max_length=512)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='api.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewed_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1028)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(upload_to='media/reviewed_books')),
                ('image', models.ImageField(upload_to='media/reviewed_books')),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1)),
                ('author', models.ManyToManyField(related_name='reviewed_books', to='api.Author')),
                ('category', models.ManyToManyField(related_name='reviewed_books', to='api.Category')),
                ('critic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('l', 'like'), ('d', 'dislike')], max_length=1)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='api.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='api.Category'),
        ),
        migrations.AddField(
            model_name='author',
            name='related_category',
            field=models.ManyToManyField(blank=True, related_name='authors', to='api.Category'),
        ),
        migrations.AddField(
            model_name='user',
            name='readlist',
            field=models.ManyToManyField(blank=True, related_name='users', to='api.Book'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
