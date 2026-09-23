from django.contrib import admin
from jobPortal.models import *

# Register your models here.
admin.site.register([
    CustomUserModel,
    RecruiterProfileModel,
    SeekerProfileModel,
    CategoryModel,
    JobPostModel,
    ApplyJobModel
])