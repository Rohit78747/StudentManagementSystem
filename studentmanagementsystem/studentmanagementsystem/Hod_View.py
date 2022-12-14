from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,SessionYear,CustomUser,Student,Staff,Subject,Staff_Notification,Student_Notification,Staff_Leave,Student_Leave,StaffFeedBack,StudentFeedBack,Attendance,AttendanceReport


@login_required(login_url='/')
def Home(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_male = Student.objects.filter(gender ='Male' ).count()
    student_gender_female = Student.objects.filter(gender ='Female').count()



    context = {
        'student_count':student_count,
        'staff_count' :staff_count,
        'course_count': course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
    }

    return render(request,'Hod/home.html',context)

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

@login_required(login_url='/')
def ViewStudent(request):
    student = Student.objects.all()

    context= {
        'student':student,
    }

    return render(request,'Hod/view_student.html',context)

@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def DeleteStudent(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,"Record Are Successfully Deleted")
    return redirect('view_student')

@login_required(login_url='/')
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

@login_required(login_url='/')
def ViewCourse(request):
    course = Course.objects.all()
    context = {
        'course' : course,
    }
    return render(request,'Hod/view_course.html',context)

@login_required(login_url='/')
def EditCourse(request,id):
    course = Course.objects.get(id = id)

    context = {
        'course' : course,
    }
    return render(request,'Hod/edit_course.html',context)

@login_required(login_url='/')
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

@login_required(login_url='/')
def DeleteCourse(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,"Course Are Deleted Successfully")
    return redirect('view_course')

@login_required(login_url='/')
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

@login_required(login_url='/')
def ViewStaff(request):
    staff = Staff.objects.all()
    context = {
        'staff':staff,
    }

    return render(request,'Hod/view_staff.html',context)

@login_required(login_url='/')
def EditStaff(request,id):
    staff = Staff.objects.get( id = id)

    context ={
        'staff':staff,
    }

    return render(request,'Hod/edit_staff.html',context)

@login_required(login_url='/')
def UpdateStaff(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id = staff_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.middle_name = middle_name
        staff.gender = gender
        staff.address = address

        staff.save()
        messages.success(request,"Staff Is Successfully Updated")
        return redirect('view_staff')

    return render(request,'Hod/edit_staff.html')

@login_required(login_url='/')
def DeleteStaff(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,"Record Are Successfully Deleted")
    return redirect('view_staff')


@login_required(login_url='/')
def AddSubject(request):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id=staff_id)
        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )

        subject.save()
        messages.success(request,"Subject Are Added Successfully")
        return redirect('add_subject')

    context = {
        'course':course,
        'staff':staff,
    }
    return render(request,'Hod/add_subject.html',context)

@login_required(login_url='/')
def ViewSubject(request):

    subject = Subject.objects.all()
    context = {
        'subject':subject,
    }

    return render(request,'Hod/view_subject.html',context)

@login_required(login_url='/')
def EditSubject(request,id):
    subject = Subject.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject':subject,
        'course': course,
        'staff': staff
    }

    return render(request,'Hod/edit_subject.html',context)

@login_required(login_url='/')
def UpdateSubject(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id=staff_id)
        subject = Subject(
            id = subject_id,
            name = subject_name,
            course = course,
            staff = staff
        )
        subject.save()
        messages.success(request,"Subject Are Successfully Updated")

    return redirect('view_subject')

@login_required(login_url='/')
def DeleteSubject(request,id):
    subject = Subject.objects.filter(id = id)
    subject.delete()
    messages.success(request,"Subject Are Successfully Deleted")
    return redirect('view_subject')

@login_required(login_url='/')
def AddSession(request):
    if request.method == 'POST':
        session_year_start =request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        session = SessionYear(
            session_start = session_year_start,
            session_end =session_year_end
        )
        session.save()
        messages.success(request,"Session Year Successfully Added")
        return redirect('add_session')
    return render(request,'Hod/add_session.html')

@login_required(login_url='/')
def ViewSession(request):
    session = SessionYear.objects.all()

    context = {
        'session' : session,
    }
    return render(request,'Hod/view_session.html',context)

@login_required(login_url='/')
def EditSession(request,id):
    session = SessionYear.objects.filter(id = id)
    context = {
        'session':session,
    }
    return render(request,'Hod/edit_session.html',context)

@login_required(login_url='/')
def UpdateSession(request):
    if request.method == 'POST':

        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = SessionYear(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end
        )
        session.save()
        messages.success(request,"Session Year Updated Successfully")
        return redirect('view_session')


@login_required(login_url='/')
def DeleteSession(request,id):
    session = SessionYear.objects.get(id = id)
    session.delete()
    messages.success(request,"Session Year Successfully Deleted")

    return redirect('view_session')

@login_required(login_url='/')
def Staff_Send_Notification(request):

    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'staff':staff,
        'see_notification':see_notification,
    }
    return render(request,'Hod/send_staff_notification.html',context)

@login_required(login_url='/')
def Student_Send_Notification(request):
    student =Student.objects.all()
    see_notification = Student_Notification.objects.all()
    context = {
        'student':student,
        'see_notification':see_notification
    }

    return render(request, 'Hod/student_notification.html',context)

@login_required(login_url='/')
def Staff_Save_Notification(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)
        notification =  Staff_Notification(
            staff_id = staff,
            message = message
        )
        notification.save()
        messages.success(request,"Notification Are Successfully Sent")
        return redirect('staff_send_notification')

@login_required(login_url='/')
def Student_Save_Notification(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')

        student = Student.objects.get(admin=student_id)
        notification = Student_Notification(
            student_id=student,
            message=message
            )
        notification.save()
        messages.success(request, "Notification Are Successfully Sent")
        return redirect('student_send_notification')


@login_required(login_url='/')
def Staff_Leave_View(request):
    staff_leave = Staff_Leave.objects.all()

    context = {
        'staff_leave': staff_leave
    }

    return render(request,'Hod/staff_leave.html',context)

@login_required(login_url='/')
def StaffApproveLeave(request,id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staff_save_leave_view')

@login_required(login_url='/')
def StaffDisApproveLeave(request,id):
    leave = Staff_Leave.objects.get(id = id)
    leave.status=2
    leave.save()
    return redirect('staff_save_leave_view')

@login_required(login_url='/')
def Student_Leave_View(request):
    student_leave = Student_Leave.objects.all()

    context = {
        'student_leave': student_leave
    }

    return render(request,'Hod/student_leave.html',context)

@login_required(login_url='/')
def StudentApproveLeave(request,id):
    leave = Student_Leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('student_save_leave_view')

@login_required(login_url='/')
def StudentDisApproveLeave(request,id):
    leave = Student_Leave.objects.get(id = id)
    leave.status=2
    leave.save()
    return redirect('student_save_leave_view')


@login_required(login_url='/')
def Staff_Feedback(request):
    feedback = StaffFeedBack.objects.all()
    feedback_history =StaffFeedBack.objects.all().order_by('-id')[0:5]

    context ={
        'feedback':feedback,
        'feedback_history': feedback_history,
    }


    return render(request,'Hod/staff_feedback.html',context)

@login_required(login_url='/')
def Student_Feedback(request):
    feedback = StudentFeedBack.objects.all()
    feedback_history = StudentFeedBack.objects.all().order_by('-id')[0:5]

    context ={
        'feedback':feedback,
        'feedback_history':feedback_history,
    }
    return render(request,'Hod/student_feedback.html',context)

@login_required(login_url='/')
def Staff_Feedback_Save(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = StaffFeedBack.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        messages.success(request, "Feedback Successfully Sent")

        return redirect('staff_feedback_reply')

@login_required(login_url='/')
def Student_Feedback_Save(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')
        feedback = StudentFeedBack.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status=1
        feedback.save()
        messages.success(request, "Feedback Successfully Sent")

        return redirect('student_feedback_reply')



@login_required(login_url='/')
def Hod_View_Attendance(request):

    subject = Subject.objects.all()

    session_year = SessionYear.objects.all()

    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    attendance_date = None
    attendance_report = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = SessionYear.objects.get(id=session_year_id)

            attendance = Attendance.objects.filter(subject_id=get_subject, attendance_date=attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = AttendanceReport.objects.filter(attendance_id=attendance_id)

    context = {
        'subject': subject,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }
    return render(request,'Hod/view_attendance.html',context)