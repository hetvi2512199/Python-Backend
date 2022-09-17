from __future__ import division
from core import models as core_models
from rest_framework import serializers
from core import constants as core_constants


class SchoolSerializer(serializers.Serializer):
    school_name = serializers.CharField(max_length=50)
    pincode  = serializers.CharField(max_length=50)
    school_address = serializers.CharField(max_length = 50)

    def validate_school_name(self,value):
        school_instance =  core_models.School.objects.filter(school_name = value).last()
        if school_instance:
            raise serializers.ValidationError('school already exist')
        return value 

class UpdateSerializer(serializers.Serializer):
    school_id = serializers.IntegerField()
    school_name = serializers.CharField(max_length=50)
    pincode  = serializers.CharField(max_length=50)
    school_address = serializers.CharField(max_length = 50)
 
    def validate_school_id(self,value):
        school_instance = core_models.School.objects.filter( id = value).last()
        if not school_instance:
            raise serializers.ValidationError("school not exist")
        return school_instance    

class CollageSerializer(serializers.Serializer):
    collage_name = serializers.CharField(max_length = 20)
    code = serializers.CharField(max_length = 20)
    collages_type = serializers.ChoiceField(
            choices = core_constants.COLLAGE_CHOICE)
    city = serializers.CharField(max_length = 20)

    def validate_collage_name( self , value):
        collage_instance = core_models.Collages.objects.filter(collage_name = value).last()
        if collage_instance:
            raise serializers.ValidationError("collage already exist")
        return value    

class UpdateCollageSerializer(serializers.Serializer):
    collage_id = serializers.IntegerField()
    collage_name = serializers.CharField(max_length = 20)
    code = serializers.CharField(max_length = 20)
    collages_type = serializers.ChoiceField(
            choices = core_constants.COLLAGE_CHOICE)
    city = serializers.CharField(max_length = 20)    

    def validate_collage_id(self ,value):
        collage_instance  = core_models.Collages.objects.filter(id = value).last()
        if not collage_instance :
            raise serializers.ValidationError("collage doesn't exist")
        return collage_instance    

class StudentSerializer(serializers.Serializer):    
    student_school_collage_id = serializers.IntegerField()
    student_name = serializers.CharField(max_length = 50)
    student_roll_no = serializers.IntegerField()
    student_admission_year = serializers.CharField(max_length = 20)
    type = serializers.ChoiceField(
        choices = core_constants.TYPE)
    student_address = serializers.CharField(max_length=50)    
    grade = serializers.CharField(max_length=10)
    enrollment_number = serializers.CharField(min_length=12)
    std = serializers.ChoiceField(choices = core_constants.STUDENT_STD_TYPE) 
    division = serializers.ChoiceField(choices = core_constants.DIVISION_TYPE)  


    def validate(self,validated_data):
        type = validated_data.get("type")
        student_school_collage_id = validated_data.get('student_school_collage_id')
        enrollment_number = validated_data.get("enrollment_number")

        student_instance = core_models.Student.objects.filter(enrollment_number=enrollment_number).last()
        if student_instance:
            raise serializers.ValidationError("This enrollment already exist")

        if type == core_constants.SCHOOL_STUDENT:
            school_collage = core_models.School.objects.filter(id = student_school_collage_id).last()

        else:
            school_collage = core_models.Collages.objects.filter(id = student_school_collage_id).last()

        validated_data.update({"student_school_collage_id":school_collage}) 


        std = validated_data.get("std")
        division = validated_data.get("division")

        course_instance = core_models.Course.objects.filter(standard__std = std,standard__division = division).last()
        if not course_instance:
            raise serializers.ValidationError("Course dose not  exist for this standard")

        return validated_data




class SubjectSerializer(serializers.Serializer):
    subject_name = serializers.CharField(max_length=50)
    subject_code = serializers.CharField(max_length=10)
    is_active = serializers.BooleanField(default=False)

    def validate_subject_name(self,value):

        subject_instance = core_models.Subject.objects.filter(subject_name = value).last()
        if subject_instance:
             raise serializers.ValidationError("Subject already exist")
        return value


class SubjectUpdateSerializer(serializers.Serializer):
    subject_id = serializers.IntegerField()
    subject_name = serializers.CharField(max_length=50)
    subject_code = serializers.CharField(max_length=10)
    is_active = serializers.BooleanField(default=False)

    def validate_subject_id(self,value):
        subject_instance = core_models.Subject.objects.filter(id= value).last()
        if not subject_instance:
            raise serializers.ValidationError("Subject does not exist")
        return subject_instance    


class StandardSerializer(serializers.Serializer):
    standard_id = serializers.IntegerField()
    std = serializers.ChoiceField(choices = core_constants.STUDENT_STD_TYPE) 
    division = serializers.ChoiceField(choices = core_constants.DIVISION_TYPE)  

    def validate(self,validated_data):
        std = validated_data.get("std")
        division = validated_data.get("division")
        
        standard_instance = core_models.Standard.objects.filter(std = std,division=division)
        if standard_instance:
           raise serializers.ValidationError("This Standard & Division already exist")
  
        return validated_data



class CourseSerializer():
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=50)
