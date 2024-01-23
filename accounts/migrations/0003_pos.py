# Generated by Django 4.0.3 on 2022-04-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_document_userregistrationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='POS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('noun_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('verb_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('adjective_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('adverb_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('article_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('proposition_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('space_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('pronoun_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('Question_word_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('punctation_counter', models.DecimalField(decimal_places=2, max_digits=1000)),
            ],
        ),
    ]