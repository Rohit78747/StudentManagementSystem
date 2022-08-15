from django.contrib import messages
from django.shortcuts import render,redirect

from app.models import Student, Student_Notification,StudentFeedBack,Student_Leave,Subject,Attendance,AttendanceReport,StudentResult


def Home(request):
    return render(request,'Student/Home.html')

def StudentNotifications(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

        notification = Student_Notification.objects.filter(student_id=student_id)
        context = {
            'notification': notification
        }

        return render(request,'Student/notification.html',context)

def MarkAsDone(request,status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('student_notifications')


def StudentFeedback(request):

    student_id = Student.objects.get(admin = request.user.id)
    feedback_history =StudentFeedBack.objects.filter(student_id=student_id)
    context = {
        'feedback_history':feedback_history,
    }

    return render(request,'Student/feedback.html',context)

def StudentFeedbackSave(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        student = Student.objects.get(admin = request.user.id)
        feedBack =StudentFeedBack(
            student_id = student,
            feedback =feedback,
            feedback_reply = '',
        )
        feedBack.save()

        return redirect('student_feedback')

def ApplyLeave(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id

        student_leave_history = Student_Leave.objects.filter(student_id=student_id)

        context = {
            'student_leave_history': student_leave_history
        }
        return render(request, 'Student/apply_leave.html',context)


def ApplyLeaveSave(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student = Student.objects.get(admin = request.user.id)
        leave = Student_Leave(
            student_id = student,
            date = leave_date,
            message = leave_message
        )
        leave.save()
        messages.success(request,"Successfully Applied For Leave")
        return redirect('student_apply_leave')

def Student_View_Attendance(request):
    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course=student.course_id)

    action = request.GET.get('action')
    get_subject = None
    attendance_report = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')

            get_subject = Subject.objects.get(id=subject_id)



            attendance_report = AttendanceReport.objects.filter(student_id=student,attendance_id__subject_id=subject_id)


    context={
        'subjects':subjects,
        'action':action,
        'get_subject': get_subject,
        'attendance_report':attendance_report,
    }

    return render(request,'Student/view_attendance.html',context)


def Student_View_Result(request):

    student = Student.objects.get(admin = request.user.id)

    result = StudentResult.objects.filter(student_id=student)
    mark = None
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        mark = assignment_mark+exam_mark



    context = {
        'result':result,
        'mark':mark
    }
    return render(request,'Student/view_result.html',context)


