from django.db import models
import uuid


class login_info(models.Model):
    userID = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)


class doctor_info(models.Model):
    userID = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)


class patient_info(models.Model):
    user = models.OneToOneField(to=login_info, related_name='user', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birthday = models.DateField()
    phone = models.CharField(max_length=50)
    marriage = models.BooleanField()
    history = models.BooleanField()
    emergency_name = models.CharField(max_length=50)
    emergency_phone = models.CharField(max_length=50)
    address = models.TextField()


class symptom_info(models.Model):
    user = models.OneToOneField(to=login_info, related_name='user2', on_delete=models.CASCADE)
    TYPE_CHOICE = (
        (u'F', u'Familial'),
        (u'E', u'Early-onset'),
        (u'L', u'Late-onset'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICE)
    symptom = models.CharField(max_length=50)
    description = models.TextField()


class moca_info(models.Model):
    mocaID = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(to=login_info, related_name='user3', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=10)
    question_1_1 = models.TextField()
    question_1_2 = models.TextField()
    question_1_3 = models.TextField()
    question_2_1 = models.CharField(max_length=20)
    question_2_2 = models.CharField(max_length=20)
    question_2_3 = models.CharField(max_length=20)
    question_3_1 = models.TextField()
    question_4_1 = models.TextField()
    question_4_2 = models.TextField()
    question_4_3 = models.CharField(max_length=50)
    question_4_4 = models.CharField(max_length=20)
    question_5_1 = models.TextField()
    question_5_2 = models.TextField()
    question_5_3 = models.TextField()
    question_6_1 = models.CharField(max_length=100)
    question_3_2_1 = models.CharField(max_length=100)
    question_3_2_2 = models.TextField()
    question_7_1 = models.CharField(max_length=100)
