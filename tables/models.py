import datetime
import os

from django.contrib.auth.models import User
from django.db import models


def user_upload_path(instance, filename):
    # Determine the model type and use it to create a unique directory structure
    if isinstance(instance, KPI_1):
        model_type = "kpi_1"
    elif isinstance(instance, KPI_2):
        model_type = "kpi_2"
    elif isinstance(instance, KPI_3):
        model_type = "kpi_3"
    elif isinstance(instance, KPI_4):
        model_type = "kpi_4"
    elif isinstance(instance, KPI_5):
        model_type = "kpi_5"
    elif isinstance(instance, KPI_6):
        model_type = "kpi_6"
    elif isinstance(instance, KPI_7):
        model_type = "kpi_7"
    elif isinstance(instance, KPI_8):
        model_type = "kpi_8"
    elif isinstance(instance, KPI_9):
        model_type = "kpi_9"
    else:
        model_type = "unknown"  # You can handle other model types as needed

    return f'user_uploads/{model_type}/{instance.id}/{filename}'
    
class TeachersAddInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='profile/avatars/', null=True, blank=True)
    degree = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    school = models.CharField(max_length=100)

# Create your models here.
class KPI_1(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi1')
    publication =  [
        ('1', 'Публикация статьи в рецензируемых научных изданиях 1-4 квартиля, входящих в базу данных Web of Science (СА) или имеющих процентиль по Cite Score в базе Scopus не менее 35 или индексируемых в Social Science Citation Index и (или) индексируемых в Arts and Humanities Citation Index (лично/в соавторстве)'),
        ('2', 'Публикация статьи в рецензируемых научных изданиях 1-4 квартиля, входящих в базу данных Web of Science (СА) или имеющих процентиль по Cite Score в базе Scopus не менее 25 или индексируемых в Social Science Citation Index и (или) индексируемых в Arts and Humanities Citation Index (лично/в соавторстве)'),
        ('3', 'Публикация ППС AlmaU совместно с вузами партнерами Cintana Alliance в рецензируемых научных изданиях, индексируемых базами данных Scopus и (или) WoS'),
        ('4', 'Публикации в рецензируемых научных изданиях, индексируемых базами данных Scopus и (или) WoS (лично/в соавторстве) в журналах/сборниках конференций'),
        ('5', 'Публикация статьи в журналах, рекомендованных Комитетом по обеспечению качества в сфере образования и науки (лично/в соавторстве')                                                                                                            
    ]
    publication_choise = models.TextField( choices=publication, default='')
    title_of_the_article = models.CharField( max_length=60)
    name = models.CharField( max_length=100)
    surname = models.CharField( max_length=100)
    name_of_the_magazine = models.CharField( max_length=100)
    year_of_publication = models.IntegerField()
    link = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to=user_upload_path)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        # Проверяем значение publication_choose и устанавливаем points соответственно
        if self.publication_choise == '1':
            self.points = '40'  # Здесь установите значение, которое соответствует выбору '1'
        elif self.publication_choise == '2':
            self.points = '35'  # Здесь установите значение, которое соответствует выбору '2'
        elif self.publication_choise == '3':
            self.points = '25'  # Здесь установите значение, которое соответствует выбору '3'
        elif self.publication_choise == '4':
            self.points = '25'  # Здесь установите значение, которое соответствует выбору '4'
        elif self.publication_choise == '5':
            self.points = '10'  # Здесь установите значение, которое соответствует выбору '5'
        super().save(*args, **kwargs)


    def publish(self):
        self.save()

    def __str__(self):
        return self.link

class KPI_2(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi2')
    literature = [
        ('1', 'Издание монографии: - рекомендованные Ученым советом AlmaU (лично/в соавторстве)  - в зарубежных издательствах на иностранных языках (лично/в соавторстве) (Отсутствие соавторства с ППС, участвующие в системе KPI, для оценки принимается монография объемом не менее 5 печатных листов с личным вкладом автора не менее 3 печатных листов; для оценки принимаются не более 1 рукописи)'),
        ('2', 'Издание учебника или учебного пособия, рекомендованного Учебно-методическим объединением Республиканского учебно-методического совета Министерства науки и высшего образования Республики Казахстан (Отсутствие соавторства с ППС, участвующие в системе KPI; для оценки принимаются не более 1 рукописи)'),
        ('3', 'Издание учебника или учебного пособия, рекомендованного Ученым советом AlmaU (Отсутствие соавторства с ППС, участвующие в системе KPI; для оценки принимаются не более 1 рукописи)')
    ]
    literature_choise = models.TextField( choices=literature, default='')
    title_of_the_monograph = models.CharField( max_length=60)
    year_of_publication = models.IntegerField()
    name_of_publication = models.CharField(max_length=100)
    number_of_printed_sheets = models.IntegerField()
    uploaded_monography = models.FileField(upload_to=user_upload_path)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        # Проверяем значение publication_choose и устанавливаем points соответственно
        if self.literature_choise == '1':
            self.points = '20'  # Здесь установите значение, которое соответствует выбору '1'
        elif self.literature_choise == '2':
            self.points = '20'  # Здесь установите значение, которое соответствует выбору '2'
        elif self.literature_choise == '3':
            self.points = '10'  # Здесь установите значение, которое соответствует выбору '3'
        super().save(*args, **kwargs)

    def publish(self):
        self.save()

    def __str__(self):
        return self.number_of_printed_sheets

class KPI_3(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi3')
    researches = [
        ('1', 'Участие в научно-исследовательских проектах, финансируемых из государственного бюджета (Руководитель/исполнитель проекта) (Проект должен быть одобрен, не учитывается участие в подготовке заявки)'),
        ('2', 'Участие в научно-исследовательских проектах, финансируемых из внебюджетных средств с обязательной аффилиацией AlmaU (Руководитель/исполнитель проекта) (Проект должен быть одобрен, не учитывается участие в подготовке заявки)'),
        ('3', 'Участие в международных научно-исследовательских проектах с обязательной аффилиацией AlmaU, в том числе в проектах Cintana и вузов партнеров Cintana Alliance (Руководитель/исполнитель проекта) (Проект должен быть одобрен, не учитывается участие в подготовке заявки)'),
        ('4', 'Подготовка конкурсной заявки на грантовый научно-исследовательский проект, прошедший процедуру внутренней экспертизы, рекомендованной для подачи от AlmaU в конкурс и прошедшей процедуру ГНТЭ, но отклоненной ННС')
    ]
    researches_choise = models.TextField( choices=researches, default='')
    title_of_the_project = models.CharField( max_length=60)
    number_of_the_project = models.IntegerField()
    years_of_completion = models.CharField( max_length=100)
    role =  [
        ('director', 'Руководитель'),
        ('executor', 'Исполнитель'),
    ]
    role_in_the_project = models.CharField(max_length=10, choices=role)
    director_of_the_project = models.CharField(max_length=40)
    copy_of_the_contract = models.FileField(upload_to=user_upload_path)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        # Проверяем значение publication_choose и устанавливаем points соответственно
        if self.researches_choise == '1':
            self.points = '40'  # Здесь установите значение, которое соответствует выбору '1'
        elif self.researches_choise == '2':
            self.points = '40'  # Здесь установите значение, которое соответствует выбору '2'
        elif self.researches_choise == '3':
            self.points = '30'  # Здесь установите значение, которое соответствует выбору '3'
        elif self.researches_choise == '4':
            self.points = '15'
        super().save(*args, **kwargs)

    def publish(self):
        self.save()

    def __str__(self):
        return self.director_of_the_project

class KPI_4(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi4')
    countries = [
        ('1', 'Казахстан'),
        ('2', 'Зарубежные страны')
    ]
    countries_choise = models.TextField( choices=countries, default='')
    event_title = models.CharField( max_length=60)
    event_date = models.DateField()
    format =  [
        ('online', 'Онлайн'),
        ('offline', 'Оффлайн'),
    ]
    format_of_the_event = models.CharField(max_length=100, choices=format)
    country = models.CharField(max_length=50)
    organisations_holding_event = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    event_program = models.FileField(upload_to=user_upload_path)
    title_of_the_report = models.CharField(max_length=50)
    copy_of_the_report = models.FileField(upload_to=user_upload_path)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        # Проверяем значение publication_choose и устанавливаем points соответственно
        if self.countries_choise == '1':
            self.points = '10'  # Здесь установите значение, которое соответствует выбору '1'
        elif self.countries_choise == ' 2':
            self.points = '20'  # Здесь установите значение, которое соответствует выбору '2'
        super().save(*args, **kwargs)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title_of_the_report

class KPI_5(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi5')
    name_of_the_doctoral_student = models.CharField( max_length=60)
    surname_of_the_doctoral_student = models.CharField( max_length=60)
    university_of_doctoral_studies = models.CharField( max_length=100)
    faculty_of_doctoral_student = models.CharField( max_length=100)
    year_of_the_beginning_of_studies = models.IntegerField()
    year_of_graduation = models.IntegerField()
    topic_of_the_dissertation = models.CharField(max_length=40)
    decision_of_the_academic_council_on_scientific_guidance = models.FileField(upload_to=user_upload_path)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def publish(self):
        self.save()

    def __str__(self):
        return self.topic_of_the_dissertation

class KPI_6(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi6')
    name_of_the_doctoral_student = models.CharField( max_length=60)
    surname_of_the_doctoral_student = models.CharField( max_length=60)
    school = models.CharField( max_length=100)
    topic_of_the_dissertation = models.CharField( max_length=100)
    year_of_award = models.IntegerField()
    decision_of_the_authorized_body_on_awarding_an_academic_degree = models.FileField(upload_to=user_upload_path)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def publish(self):
        self.save()

    def __str__(self):
        return self.year_of_award

class KPI_7(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi7')
    decision_of_the_authorized_body_on_awarding_an_academic_degree_in_the_field_of_art_or_sports = models.FileField(upload_to=user_upload_path)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def publish(self):
        self.save()

    def __str__(self):
        return self.decision_of_the_authorized_body_on_awarding_an_academic_degree_in_the_field_of_art_or_sports


class KPI_8(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi8')
    decision_of_the_AlmaU_School_or_management_on_the_scientific_management_of_the_laboratory_or_center = models.FileField(upload_to=user_upload_path)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def publish(self):
        self.save()

    def __str__(self):
        return self.decision_of_the_AlmaU_School_or_management_on_the_scientific_management_of_the_laboratory_or_center     

class KPI_9(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kpi9')
    name_of_the_patent = models.CharField( max_length=60)
    year_of_receipt = models.IntegerField()
    number_of_the_patent = models.IntegerField()
    copy_of_the_security_document = models.FileField(upload_to=user_upload_path)
    the_object_for_which_the_security_document_was_received = models.CharField(max_length=40)
    points = models.CharField(default='40', max_length=10, editable=False)
    date = models.DateField(default=datetime.date.today)

    def publish(self):
        self.save()

    def __str__(self):
        return self.the_object_for_which_the_security_document_was_received  