from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from .models import Student
import csv

class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'student_name', 'exam_name', 'total', 'result', 'mediam')
    search_fields = ('roll_number', 'student_name', 'exam_name')
    list_filter = ('exam_name', 'result', 'mediam')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('bulk-upload-results/', self.admin_site.admin_view(self.bulk_upload_results), name='bulk_upload_results'),
            path('bulk-upload-halltickets/', self.admin_site.admin_view(self.bulk_upload_halltickets), name='bulk_upload_halltickets'),
        ]
        return custom_urls + urls

    # Bulk upload for results
    def bulk_upload_results(self, request):
        if request.method == "POST":
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                roll_number = row.get('roll_number')
                student_name = row.get('student_name')
                exam_name = row.get('exam_name')
                sub1 = row.get('sub1')
                sub2 = row.get('sub2')
                sub3 = row.get('sub3')
                sub4 = row.get('sub4')
                total = row.get('total')
                result = row.get('result')

                if roll_number:
                    student, created = Student.objects.get_or_create(roll_number=roll_number)
                    if student_name:
                        student.student_name = student_name
                    if exam_name:
                        student.exam_name = exam_name
                    if sub1:
                        student.sub1 = int(sub1)
                    if sub2:
                        student.sub2 = int(sub2)
                    if sub3:
                        student.sub3 = int(sub3)
                    if sub4:
                        student.sub4 = int(sub4)
                    if total:
                        student.total = int(total)
                    if result:
                        student.result = result
                    student.save()
            return redirect('/admin/portal/student/')
        return render(request, 'portal/bulk_upload_results.html')

    # Bulk upload for hall tickets
    def bulk_upload_halltickets(self, request):
        if request.method == "POST":
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                roll_number = row.get('roll_number')
                student_name = row.get('student_name')
                exam_name = row.get('exam_name')
                mediam = row.get('mediam')
                exam_address = row.get('exam_address')
                mobile_number = row.get('mobile_number')
                stud_address = row.get('stud_address')

                if roll_number:
                    student, created = Student.objects.get_or_create(roll_number=roll_number)
                    if student_name:
                        student.student_name = student_name
                    if exam_name:
                        student.exam_name = exam_name
                    if mediam:
                        student.mediam = mediam
                    if exam_address:
                        student.exam_address = exam_address
                    if mobile_number:
                        student.mobile_number = mobile_number
                    if stud_address:
                        student.stud_address = stud_address
                    student.save()
            return redirect('/admin/portal/student/')
        return render(request, 'portal/bulk_upload_halltickets.html')

admin.site.register(Student, StudentAdmin)
