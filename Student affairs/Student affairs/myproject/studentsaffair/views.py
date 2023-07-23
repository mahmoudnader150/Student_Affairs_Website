from django.shortcuts import render

from studentsaffair.models import Student

# Create your views here.


def index(request):
    return render(request, 'studentsaffair/index.html')


def main(request):
    return render(request, 'studentsaffair/MainPage.html')


def home(request):
    return render(request, 'studentsaffair/HomePage.html')


def activity(request):
    if request.method == "POST":
        print(request.POST.get("active"))
        Student.objects.filter(student_id=request.POST.get(
            "student_id")).update(active="Active" if request.POST.get("active") == "InActive" else "InActive")
    return render(request, 'studentsaffair/Activitystatus.html', {
        "students": Student.objects.all()
    })


def search(request):
    context = {
        'students': Student.objects.filter(active="Active")
    }
    return render(request, 'studentsaffair/SearchInfo_Table.html', context)


def assign(request):
    if request.method == "POST":
        Student.objects.filter(student_id=request.POST.get("student_id")).update(
            department=request.POST.get("Department"))
    return render(request, 'studentsaffair/student_assignment.html')


def update(request):
    if request.method == "POST":
        if request.POST.get("m") == "U":
            print('UPDATE')
            print("name: ", request.POST.get('name'))
            print("student_id: ", request.POST.get('student_id'))
            print("email: ", request.POST.get('email'))
            print("mobile: ", request.POST.get('mobile'))
            print("active: ", request.POST.get('active'))
            print("level: ", request.POST.get('level'))
            print("date_of_birth: ", request.POST.get('date_of_birth'))
            print("gpa: ", request.POST.get('gpa'))
            print("gender: ", request.POST.get('gender'))
            print("department: ", request.POST.get('department'))
            if request.POST.get('name') and request.POST.get('student_id') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('active') and request.POST.get('level') and request.POST.get('date_of_birth') and request.POST.get('gpa') and request.POST.get('gender') and request.POST.get('department'):
                Student.objects.filter(student_id=request.POST.get('student_id')).update(
                    name=request.POST.get('name'),
                    date_of_birth=request.POST.get('date_of_birth'),
                    mobile=request.POST.get('mobile'),
                    email=request.POST.get('email'),
                    active=request.POST.get('active'),
                    level=request.POST.get('level'),
                    gpa=request.POST.get('gpa'),
                    gender=request.POST.get('gender'),
                    department=request.POST.get('department')
                )
        elif request.POST.get("m") == "D":
            print('DELETE')
            if request.POST.get('student_id'):
                Student.objects.filter(
                    student_id=request.POST.get('student_id')).delete()
    return render(request, 'studentsaffair/UpdateDelete.html')


def Add(request):
    # name = request.POST['name']
    # date = request.POST['date']
    # gpa = request.POST['gpa']
    # Gender = request.POST['Gender']
    # Student_Level = request.POST['Student Level']
    # Student_Status = request.POST['Student Status']
    # Department = request.POST['Department']
    # email = request.POST['email']
    # number = request.POST['number']
    # students = Student.objects.all()
    # , {'students': students}
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('student_id') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get('active') and request.POST.get('level') and request.POST.get('date_of_birth') and request.POST.get('gpa') and request.POST.get('gender') and request.POST.get('department'):
            s = Student(
                name=request.POST.get('name'),
                student_id=request.POST.get('student_id'),
                email=request.POST.get('email'),
                gender=request.POST.get('gender'),
                department=request.POST.get('department'),
                mobile=request.POST.get('mobile'),
                active=request.POST.get('active'),
                level=request.POST.get('level'),
                date_of_birth=request.POST.get('date_of_birth'),
                gpa=request.POST.get('gpa')
            )
            s.save()
        else:
            pass
    return render(request, 'studentsaffair/Add_New_Student_Page.html')
