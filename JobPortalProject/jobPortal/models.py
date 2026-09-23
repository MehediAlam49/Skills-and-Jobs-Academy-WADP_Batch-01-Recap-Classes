from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPES=[
        ('Recruiter', 'Recruiter'),
        ('Seeker', 'Seeker'),
    ]
    display_name=models.CharField(max_length=100, null=True)
    user_type=models.CharField(choices=USER_TYPES, max_length=100, null=True)

    def __str__(self):
        return f'{self.username}'

class RecruiterProfileModel(models.Model):
    recruiter=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True, related_name='recruiter_profile')
    company_name=models.CharField(max_length=100, null=True)
    address=models.TextField(null=True)
    contact=models.CharField(max_length=20, null=True)
    logo=models.ImageField(upload_to='media/company_logo', null=True)

    created_at=models.DateField(auto_now_add=True, null=True)
    updated_at=models.DateField(auto_now=True, null=True)

    def __str__(self):
            return f'{self.recruiter}'

class SeekerProfileModel(models.Model):
    seeker=models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True, related_name='seeker_profile')
    address=models.TextField(null=True)
    contact=models.CharField(max_length=20, null=True)
    skill_set=models.TextField(null=True)
    profile_image=models.ImageField(upload_to='media/profile_image', null=True)

    created_at=models.DateField(auto_now_add=True, null=True)
    updated_at=models.DateField(auto_now=True, null=True)


    def __str__(self):
         return f'{self.seeker}'

class CategoryModel(models.Model):
     name=models.CharField(max_length=200, null=True)

     def __str__(self):
          return f'{self.name}'
    
# Title, Number of openings, Category,Job description, Skills set
class JobPostModel(models.Model):
     posted_by=models.ForeignKey(RecruiterProfileModel, on_delete=models.CASCADE, related_name='job_post_info', null=True)
     title=models.CharField(max_length=100, null=True)
     number_of_openings=models.PositiveBigIntegerField(null=True)
     category=models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
     description=models.TextField(null=True)
     skill_set=models.TextField(null=True)

     created_at=models.DateField(auto_now_add=True, null=True)
     updated_at=models.DateField(auto_now=True, null=True)

     def __str__(self):
          return f'{self.title}'

class ApplyJobModel(models.Model):
     applied_by=models.ForeignKey(SeekerProfileModel, on_delete=models.CASCADE, related_name='applied_by_info', null=True)
     resume=models.FileField(upload_to='media/seeker_resume')
     applied_at=models.DateField(auto_now_add=True, null=True)
     applied_job=models.ForeignKey(JobPostModel, on_delete=models.CASCADE, null=True, related_name='applied_by_info')

     def __str__(self):
          return f'{self.applied_by}'


    