from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from administrator.models import Branch
from django.utils import timezone
from coordinator.models import Companies
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
# As model field:
from django_currentuser.db.models import CurrentUserField



class Student(models.Model):
    
    name = models.CharField(max_length = 120,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    admissionNumber = models.IntegerField(primary_key=True)

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    yearOfGraduation = models.IntegerField(null=False)

    rollNumber = models.IntegerField(null=False)

    CGPA = models.FloatField(null=False)
    
    def __str__(self) :
        return str(self.admissionNumber)

    class Meta:
        db_table = 'student_user'

@receiver(post_save, sender=Student)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        my_group = Group.objects.get(name='Student')
        student = Student.objects.get(user=kwargs.get('instance').user)
        my_group.user_set.add(student.user)

class Event(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)
    time = models.DateTimeField()
    text = models.CharField(max_length=500)
    datePublished = models.DateTimeField(default=timezone.now)


class Application(models.Model):
    user = CurrentUserField()
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    def __str__(self) :
        student = Student.objects.get(user=self.user)
        return str(student)


class CompanyApplicants(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null = True)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    APPLIED = 'A'
    INTERVIEW = 'I'
    NOTAPPLIED = 'N'
    PLACED = 'P'

    APPLICATION_STATUS = (
        (APPLIED, 'Applied'),
        (INTERVIEW, 'Qualified for Interview'),
        (NOTAPPLIED, 'Not applied'),
        (PLACED, 'Placed')
    )

    placementStatus = models.CharField(
        max_length=2,
        choices=APPLICATION_STATUS,
        default=NOTAPPLIED,
    )

    def __str__(self):
        return str(self.student.admissionNumber) + " " +self.student.name + " " + self.student.user.email

    @staticmethod
    def getCompanyName(self):
        return self.company.name

    
    


