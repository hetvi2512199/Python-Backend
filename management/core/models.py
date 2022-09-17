from django.db import models
from core import constants as core_constants

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class School(BaseModel):
    school_name = models.CharField(max_length=50)
    pincode = models.IntegerField()
    school_address = models.TextField()
    
    def __str__(self):
        return self.school_name

    def school_get_details(self):
        return{
            "id":self.id,
            "school_name": self.school_name,
            "pincode": self.pincode,
            "school_address" : self.school_address,
        }    

class Collages(BaseModel):

    collage_name = models.CharField(max_length=50)
    code  = models.CharField(max_length=50)  
    collages_type = models.CharField(max_length=50,
                        choices = core_constants.COLLAGE_CHOICE)
    city = models.CharField(max_length=50)                        
    
    def __str__(self):
        return self.collage_name

    def collage_get_details(self):
        return{
            "id":self.id,
            "collage_name":self.collage_name,
            "code":self.code,
            "collages_type":self.collages_type,
            "city":self.city,
        }
            
class Student(BaseModel):
    student_name = models.CharField(max_length = 20)
    student_roll_no = models.IntegerField()
    student_admission_year = models.CharField(max_length = 20)
    type = models.CharField(max_length=20, 
                    choices = core_constants.TYPE)    
    grade = models.CharField(max_length=10)  
    enrollment_number = models.CharField(max_length=12)
    student_address = models.CharField(max_length=50)  

    collage = models.ForeignKey(
        "Collages",  on_delete=models.CASCADE , blank=True , null=True 
    )             
    school = models.ForeignKey(
        "School",  on_delete=models.CASCADE , blank=True , null=True
    )  

    def __str__(self):
        return self.student_name 

    def student_get_details(self,type=None):

        if type == core_constants.COLLAGE_STUDENT:
            return{
                "collage":self.collage.collage_get_details(),
                "student_name":self.student_name,
                "student_roll_no":self.student_roll_no,
                "student_admission_year":self.student_admission_year,
                "student_address":self.student_address,
                "grade":self.grade,
                "enrollment_number":self.enrollment_number

            }
        else:
            return{

                "school":self.school.school_get_details(),
                "student_name":self.student_name,
                "student_roll_no":self.student_roll_no,
                "student_admission_year":self.student_admission_year,
                "student_address":self.student_address,
                "grade":self.grade,
                "enrollment_number":self.enrollment_number
            }


class Subject(BaseModel):
    subject_name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=10) 
    is_active = models.BooleanField(default=False)          
         
    def __str__(self):
        return self.subject_name

    def subject_get_details(self):
        return{

            "subject_id":self.id,
            "subject_name":self.subject_name,
            "subject_code":self.subject_code,
            "is_active":self.is_active
        }
        

class Standard(BaseModel):
    std = models.CharField(max_length=10,choices = core_constants.STUDENT_STD_TYPE) 
    division = models.CharField(max_length=10,choices = core_constants.DIVISION_TYPE)   
                
    def __str__(self):
        return self.std

    def get_details(self):
        return{
            
            "std":self.std,
            "division":self.division,
        }

class Course(BaseModel):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    standard = models.ForeignKey(
        "Standard",  on_delete=models.CASCADE , blank=True , null=True 
    )         

    subject = models.ManyToManyField(
        "Subject",  blank=True , null=True 
    )         

    def __str__(self):
        return self.name

    def get_details(self):
        return{

            "name":self.name,
            "description":self.description,
            "standard":self.standard.get_details(),
            "subject":[sub_obj.subject_get_details() for sub_obj in self.subject.all()]

        }

class StudentDetails(BaseModel):
    student =  models.ForeignKey(
        "Student",  on_delete=models.CASCADE , blank=True , null=True , related_name="student_details"
    )  
    course = models.ForeignKey(
        "Course", on_delete=models.CASCADE , blank = True , null = True,related_name="student_course" 
    )

    def get_details(self):
        return{

            "student":self.student.student_get_details(),
            "course":self.course.get_details()
        }