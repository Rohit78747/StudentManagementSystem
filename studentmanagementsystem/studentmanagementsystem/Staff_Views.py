from django.contrib import messages
from django.shortcuts import render,redirect
from app.models import Staff,Staff_Notification,Staff_Leave,StaffFeedBack

def Home(request):
    return render(request,'Staff/home.html')

def Notifications(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
       staff_id = i.id

       notification = Staff_Notification.objects.filter(staff_id=staff_id)
       context = {
           'notification':notification
       }

       return render(request,'Staff/notification.html',context)

def MarkAsRead(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')

def ApplyLeave(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id

        staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)

        context={
            'staff_leave_history':staff_leave_history
        }
        return render(request,'Staff/apply_leave.html',context)


def ApplyLeaveSave(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        staff = Staff.objects.get(admin = request.user.id)
        leave = Staff_Leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message
        )
        leave.save()
        messages.success(request,"Successfully Applied For Leave")
    return redirect('staff_apply_leave')

def StaffFeedback(request):

    staff_id = Staff.objects.get(admin = request.user.id)
    feedback_history =StaffFeedBack.objects.filter(staff_id=staff_id)
    context = {
        'feedback_history':feedback_history,
    }

    return render(request,'Staff/feed_back.html',context)

def StaffFeedbackSave(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin = request.user.id)
        feedBack =StaffFeedBack(
            staff_id = staff,
            feedback =feedback,
            feedback_reply = '',
        )
        feedBack.save()

        return redirect('staff_feedback')




