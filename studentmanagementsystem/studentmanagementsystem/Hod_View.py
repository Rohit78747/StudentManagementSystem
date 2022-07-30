from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,SessionYear,CustomUser,Student,Staff


@login_required(login_url='/')
def Home(request):
    return render(request,'Hod/home.html')

@login_required(login_url='/')
def AddStudent(request):
    course = Course.objects.all()
    session_year = SessionYear.objects.all()
    if request.method == "POST":
        profile_pic =request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,"Email Is ALready Taken")
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "UserName Is ALready Taken")
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name = last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type = 3
            )

            user.set_password(password)
            user.save()
            course = Course.objects.get(id=course_id)
            session_year = SessionYear.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                middle_name=middle_name,
                address=address,
                session_id =session_year,
                course_id=course,
                gender=gender
            )
            student.save()
            messages.success(request, user.first_name+" "+user.last_name+" "+ "Successfully Added")
            return redirect('add_student')


    context = {
        'course' :course,
        'session_year' : session_year
    }
    return render(request,'Hod/add_student.html',context)


def ViewStudent(request):
    student = Student.objects.all()

    context= {
        'student':student,
    }

    return render(request,'Hod/view_student.html',context)

def EditStudent(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = SessionYear.objects.all()

    context = {
        'student' : student,
        'course': course,
        'session_year':session_year
    }
    return render(request,'Hod/edit_student.html',context)

def UpdateStudent(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.middle_name = middle_name
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        session_year = SessionYear.objects.get(id=session_year_id)
        student.session_year_id = session_year
        student.save()
        messages.success(request,"Record Updated Successfully Records !")
        return redirect('view_student')
    return render(request,'Hod/edit_student.html')

def DeleteStudent(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,"Record Are Successfully Deleted")
    return redirect('view_student')

def AddCourse(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request,"Course Are Successfully Created")
        return redirect('add_course')

    return render(request,'Hod/add_course.html')

def ViewCourse(request):
    course = Course.objects.all()
    context = {
        'course' : course,
    }
    return render(request,'Hod/view_course.html',context)

def EditCourse(request,id):
    course = Course.objects.get(id = id)

    context = {
        'course' : course,
    }
    return render(request,'Hod/edit_course.html',context)

def UpdateCourse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id =course_id)
        course.name = name
        course.save()
        messages.success(request,"Course Are Successfully Updated")
        return redirect('view_course')
    return render(request,'Hod/edit_course.html')

def DeleteCourse(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,"Course Are Deleted Successfully")
    return redirect('view_course')

def AddStaff(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email Is Already Taken")
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "UserName Is Already Taken")
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name = last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                middle_name =middle_name,
                address = address,
                gender = gender
            )
            staff.save()
            messages.success(request,'Staff Are Successfully Added !')
            return redirect('add_staff')

    return render(request,'Hod/add_staff.html')