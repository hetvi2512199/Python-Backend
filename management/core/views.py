from django.core.checks import messages
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView

from core import models as core_models
from core import serializers as core_serializer
from core import constants as core_constants
# Create your views here.




#insert
class SchoolAPIView(APIView):
    def post(self,request):
        req_data = request.data

        serializer_instance  =  core_serializer.SchoolSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status=400, data = {"message":"data not found"})


        school_name  = serializer_instance.validated_data.get("school_name")
        pincode  = serializer_instance.validated_data.get("pincode")
        school_address  = serializer_instance.validated_data.get("school_address")
       
        school_create_instance = core_models.School.objects.create(

            school_name = serializer_instance.validated_data.get('school_name'),
            pincode = serializer_instance.validated_data.get('pincode'),
            school_address = serializer_instance.validated_data.get('school_address')
        )
        return Response(status = 200, data = {"data":school_create_instance.school_get_details()})

    def get(self,request,id=None):
        
        is_all = request.GET.get('is_all')
        if is_all:
            school_instance = core_models.School.objects.all()

            data = [obj_data.get_details() for obj_data in school_instance]
            return Response(status=200, data = {"data":data})

        school_instance = core_models.School.objects.filter(id=id).last()
        if not school_instance:
            return Response(status=400, data = {"message":"data not found"})

        
        return Response(status = 200, data ={"data":school_instance.school_get_details()})

#delete
class SchoolDeleteAPIView(APIView):
    def post(self,request,id):
        school_instance = core_models.School.objects.filter(id=id).last()
        if not school_instance:
            return Response(status=400, data = {"message":"school not exits"})

        school_instance.delete()
        return Response(status = 200, data ={"message":"School successfully removed"})

#update
class SchoolUpdateAPIView(APIView):
    def post(self,request , id):
        req_data = request.data
        req_data.update({"school_id":id})

        serializer_instance = core_serializer.UpdateSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status=400, data = {"message":"school not exits"})


        school_instance = serializer_instance.validated_data.get("school_id")

        school_name = serializer_instance.validated_data.get("school_name")
        pincode = serializer_instance.validated_data.get("pincode")
        school_address = serializer_instance.validated_data.get("school_address")

        school_instance.school_name = school_name
        school_instance.pincode = pincode
        school_instance.school_address = school_address

        #save method
        school_instance.save()
        return Response(status = 200, data ={"data":school_instance.school_get_details()})

#create
class CollageAPIView(APIView):
    def post(self , request ):
        req_data = request.data

        serializer_instance = core_serializer.CollageSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status=400, data = {"message":"data not found"})

        collage_create_instance = core_models.Collages.objects.create(

            collage_name = serializer_instance.validated_data.get('collage_name'),
            code = serializer_instance.validated_data.get("code"),
            collages_type = serializer_instance.validated_data.get('collages_type'),
            city = serializer_instance.validated_data.get("city")
        )
        return Response(status = 200 ,data = {"data":collage_create_instance.collage_get_details()})

#delete
class CollageDeleteAPIView(APIView):
    def post(self,request , id):
        collage_instance = core_models.Collages.objects.filter(id = id)
        if not collage_instance:
            return Response(status=400, data = {"message":"collage not exist"})

        collage_instance.delete()
        return Response(status = 200 ,data = {"message":"Collage successfully removed"})
   
#update
class UpdateCollageAPIView(APIView):
    def post(self ,request ,id ):
        req_data = request.data
        req_data.update({"collage_id":id})

        serializer_instance = core_serializer.UpdateCollageSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status=400, data = {"message":"school not exits"})

        collage_instance = serializer_instance.validated_data.get("collage_id")

        collage_name = serializer_instance.validated_data.get("collage_name")
        code = serializer_instance.validated_data.get("code")
        collages_type = serializer_instance.validated_data.get("collages_type")
        city = serializer_instance.validated_data.get("city")

        collage_instance.collage_name = collage_name
        collage_instance.code = code
        collage_instance.collages_type = collages_type
        collage_instance.city = city

        collage_instance.save()
        return Response(status = 200 ,data = {"data":collage_instance.collage_get_details()})

#student
class StudentAPIView(APIView):
    def post(self, request):
        req_data = request.data
      
        serializer_instance = core_serializer.StudentSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status = 400, data = {"message":serializer_instance.errors})
        
        student_school_collage_id = serializer_instance.validated_data.get("student_school_collage_id")
        student_name = serializer_instance.validated_data.get("student_name")
        student_roll_no = serializer_instance.validated_data.get("student_roll_no")
        student_admission_year = serializer_instance.validated_data.get("student_admission_year")
        type = serializer_instance.validated_data.get('type')
        student_address = serializer_instance.validated_data.get('student_address')
        grade = serializer_instance.validated_data.get("grade")
        enrollment_number = serializer_instance.validated_data.get('enrollment_number')
        std= serializer_instance.validated_data.get('std')
        division = serializer_instance.validated_data.get("division")
       

        if type == core_constants.COLLAGE_STUDENT:
            student_details = core_models.Student.objects.create(
                    collage = student_school_collage_id,
                    student_name = student_name,
                    student_roll_no = student_roll_no,
                    student_admission_year = student_admission_year,
                    type = type,
                    student_address = student_address,
                    grade = grade,
                    enrollment_number = enrollment_number,                 
            )
        
        else:
            student_details = core_models.Student.objects.create(
                    school = student_school_collage_id,
                    student_name = student_name,
                    student_roll_no = student_roll_no,
                    student_admission_year = student_admission_year,
                    type = type,
                    student_address = student_address,
                    grade = grade,
                    enrollment_number = enrollment_number,                   
            )

            course_instance = core_models.Course.objects.filter(standard__std = std, standard__division = division).last()
            if not course_instance:
                return Response(status=400, data = {"message":"Course not exits"})
            
            student_instance = core_models.StudentDetails.objects.create(

                student = student_details,
                course = course_instance
            )
        return Response(status = 200 ,data = {"data":student_instance.get_details()})

    def get(self,request):
        student_id = request.GET.get('student_id')
        type = request.GET.get("type")

        student_details = None

        student_instance = core_models.Student.objects.filter(id=student_id).last()
        if student_instance:
            student_details = student_instance.student_get_details(type)

        return Response(status = 200 ,data = {"data":student_details})

#subject
class SubjectAPIView(APIView):
    def post(self,request):
        req_data = request.data

        serializer_instance = core_serializer.SubjectSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status = 400, data = {"message":serializer_instance.errors})

        subject_name = serializer_instance.validated_data.get("subject_name")
        subject_code = serializer_instance.validated_data.get("subject_code")
        is_active =  serializer_instance.validated_data.get("is_active")

        subject_create_instance = core_models.Subject.objects.create(

            subject_name = serializer_instance.validated_data.get("subject_name"),
            subject_code = serializer_instance.validated_data.get("subject_code"),
            is_active = serializer_instance.validated_data.get('is_active')
        )
        
        return Response(status = 200 ,data = {"data":subject_create_instance.subject_get_details()})


    def get(self,request):

        subject_instance = core_models.Subject.objects.filter(is_active = True)

        data = [subject_data.subject_get_details() for subject_data in subject_instance]
        return Response(status=200, data = {"data":data})

#subject delete
class SubjectDeleteAPIView(APIView):
    def post(self,request,id):
        subject_instance = core_models.Subject.objects.filter(id=id).last()
        if not subject_instance:
            return Response(status = 400, data = {"message":"subject doesn't exist"})

        subject_instance.delete()    

        return Response(status = 200 ,data = {"message":"Subject successfully removed"})

#subject update
class SubjectUpdateAPIView(APIView):
    def post(self,request,id):
        req_data = request.data
        req_data.update({"subject_id":id})

        serializer_instance = core_serializer.SubjectUpdateSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status=400, data = {"message":serializer_instance.errors})


        subject_instance = serializer_instance.validated_data.get("subject_id")

        subject_name = serializer_instance.validated_data.get("subject_name")
        subject_code = serializer_instance.validated_data.get("subject_code")
        is_active = serializer_instance.validated_data.get("is_active")

        subject_instance.subject_name = subject_name
        subject_instance.save()

        return Response(status = 200 ,data = {"data":subject_instance.subject_get_details()})

#standard
class StandardAPIView(APIView):
    def post(self,request):
        req_data = request.data

        serializer_instance = core_serializer.StandardSerializer(data = req_data)
        if not serializer_instance.is_valid():
            return Response(status=400, data = {"message":serializer_instance.errors})

        std = serializer_instance.validated_data.get("std")
        division = serializer_instance.validated_data.get("division")

        standard_create_instance = core_models.Standard.objects.create(

            std = serializer_instance.validated_data.get("std"),
            division = serializer_instance.validated_data.get("division")
        )

        return Response(status = 200 ,data = {"data":standard_create_instance.get_details()})

#course
class CourseAPIView(APIView):
    def post(self,request):
        req_data = request.data

        name = req_data.get("name")
        description = req_data.get("description")
        standard = req_data.get("standard")
        subject = req_data.get("subject")

        standard_instance = core_models.Standard.objects.filter(id = standard).last()
        if not standard_instance:
            return Response(status = 400, data = {"message":"Standard doesn't exist"})
        
       
        course_create_instance = core_models.Course.objects.create(
 
            standard = standard_instance,
            name = req_data.get("name"),
            description = req_data.get("description")

        )

        for sub_id in subject: 
            subject_instance = core_models.Subject.objects.filter(id=sub_id.get("id")).last()
            if subject_instance:
                course_create_instance.subject.add(subject_instance)

        return Response(status = 200 ,data = {"data":course_create_instance.get_details()})

class IndexAPIView(APIView):
    def get(self,request):

        Student_details = {}
        student_instance = core_models.Student.objects.filter(enrollment_number = 180941197386).last()
        if not student_instance:
            return Response(status=400, data = {"message":"Enrollment number doesn't exist"})

        student_detail = student_instance.student_details.all().last()
        student_course = student_detail.course
        student_standard = student_course.standard.get_details()
        student_subject_details = student_course.subject.all().last()

        Student_details = {

            "student":student_instance,
            "student_details":student_detail,
            "course":student_course,
            "standard":student_standard,
            "subject":student_subject_details
        }        

        return Response(status = 200, data = {"message":" We find All student details"})