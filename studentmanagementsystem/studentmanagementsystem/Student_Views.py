from django.shortcuts import render,redirect

from app.models import Student, Student_Notification,StudentFeedBack


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