# Generated by Django 5.1.4 on 2025-03-20 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_alter_article_biom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('ip', models.GenericIPAddressField(default=None, null=True)),
                ('user_agent', models.CharField(default=None, max_length=200, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='content.article')),
            ],
        ),
    ]
