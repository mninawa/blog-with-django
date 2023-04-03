# Generated by Django 4.1.5 on 2023-04-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_options_article_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='defualt/blog.jpg', upload_to='categoryPic'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog.category', verbose_name='دسته بندی'),
        ),
    ]