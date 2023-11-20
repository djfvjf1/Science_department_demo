# Generated by Django 4.1.7 on 2023-11-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_kpi_1_publication_choose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi_1',
            name='publication_choose',
            field=models.TextField(choices=[('1', 'Публикация статьи в рецензируемых научных изданиях 1-4 квартиля, входящих в базу данных Web of Science (СА) или имеющих процентиль по Cite Score в базе Scopus не менее 35 или индексируемых в Social Science Citation Index и (или) индексируемых в Arts and Humanities Citation Index (лично/в соавторстве)'), ('2', 'Публикация статьи в рецензируемых научных изданиях 1-4 квартиля, входящих в базу данных Web of Science (СА) или имеющих процентиль по Cite Score в базе Scopus не менее 25 или индексируемых в Social Science Citation Index и (или) индексируемых в Arts and Humanities Citation Index (лично/в соавторстве)'), ('3', 'Публикация ППС AlmaU совместно с вузами партнерами Cintana Alliance в рецензируемых научных изданиях, индексируемых базами данных Scopus и (или) WoS'), ('4', 'Публикации в рецензируемых научных изданиях, индексируемых базами данных Scopus и (или) WoS (лично/в соавторстве) в журналах/сборниках конференций'), ('5', 'Публикация статьи в журналах, рекомендованных Комитетом по обеспечению качества в сфере образования и науки (лично/в соавторстве')], default='', max_length=10),
        ),
    ]
