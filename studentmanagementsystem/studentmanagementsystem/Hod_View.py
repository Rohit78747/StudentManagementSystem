from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,SessionYear,CustomUser,Student


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
            messages.success(request, user.first_name+" "+user.last_name+" "+ "Sucessfully Added")
            return redirect('add_student')


    context = {
        'course' :course,
        'session_year' : session_year
    }
    return render(request,'Hod/add_student.html',context)