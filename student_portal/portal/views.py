import csv
from django.shortcuts import render, redirect
from .models import Student
from .forms import LoginForm

# View for student login
def student_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data['roll_number']
            student = Student.objects.filter(roll_number=roll_number).first()
            if student:
                request.session['student_id'] = student.id
                request.session['student_name'] = student.student_name
                return redirect('student_dashboard')
            else:
                return render(request, 'portal/login.html', {'form': form, 'error': 'Invalid Roll Number'})
    return render(request, 'portal/login.html', {'form': form})

# View for student dashboard
def student_dashboard(request):
    student_id = request.session.get('student_id')
    student_name = request.session.get('student_name')  # Fetch the name from the session
    if not student_id:
        return redirect('student_login')
    student = Student.objects.get(id=student_id)
    return render(request, 'portal/dashboard.html', {
        'student': student,
        'student_name': student_name
    })

# View for displaying the result
def view_result(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')
    student = Student.objects.get(id=student_id)
    return render(request, 'portal/result.html', {'student': student})

def download_result(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')
    student = Student.objects.get(id=student_id)
    return render(request, 'portal/result.html', {'student': student})

# View for bulk uploading results via CSV
def bulk_upload_results(request):
    if request.method == "POST":
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            student, created = Student.objects.get_or_create(roll_number=row['roll_number'])
            student.student_name = row.get('student_name', '')
            student.exam_name = row.get('exam_name', '')
            student.sub1 = int(row.get('sub1', 0))
            student.sub2 = int(row.get('sub2', 0))
            student.sub3 = int(row.get('sub3', 0))
            student.sub4 = int(row.get('sub4', 0))
            student.total = int(row.get('total', 0))
            student.result = row.get('result', '')
            student.save()
        return redirect('/admin/')
    return render(request, 'portal/bulk_upload_results.html')

# View for bulk uploading hall tickets via CSV
def bulk_upload_halltickets(request):
    if request.method == "POST":
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            student, created = Student.objects.get_or_create(roll_number=row['roll_number'])
            student.student_name = row.get('student_name', '')
            student.exam_name = row.get('exam_name', '')
            student.mediam = row.get('mediam', '')
            student.exam_address = row.get('exam_address', '')
            student.mobile_number = row.get('mobile_number', '')
            student.stud_address = row.get('stud_address', '')
            student.save()
        return redirect('/admin/')
    return render(request, 'portal/bulk_upload_halltickets.html')

# View for downloading the hall ticket
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

def download_hallticket(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    exam_address_parts = student.exam_address.split(',')
    city = exam_address_parts[0] if exam_address_parts else ''

    return render(request, 'portal/hallticket.html', {
        'student': student,
        'city': city,
    })

def generate_hallticket_pdf(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    exam_address_parts = student.exam_address.split(',')
    city = exam_address_parts[0] if exam_address_parts else ''

    template = get_template('portal/hallticket.html')
    html_content = template.render({
        'student': student,
        'city': city
    })

    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="hallticket_{student.roll_number}.pdf"'

    return response