# Generated by Django 4.2.6 on 2023-11-04 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quiz_test", "0003_category_question_category"),
    ]

    operations = [
        migrations.RenameModel(old_name="Category", new_name="QuestionCategory",),
        migrations.RemoveField(model_name="question", name="category",),
        migrations.RemoveField(model_name="userscore", name="user",),
        migrations.DeleteModel(name="Choice",),
        migrations.DeleteModel(name="Question",),
        migrations.DeleteModel(name="UserScore",),
    ]
