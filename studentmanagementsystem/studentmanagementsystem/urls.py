"""studentmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, Hod_View,Staff_Views,Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.Base,name='Base'),
#     Login path
    path('',views.Login,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='doLogout'),

    #profile Update

    path('profile',views.Profile,name='profile'),
    path('profile/update',views.Profile_Update,name='profile_update'),

    #This is hod panel url
    path('HOD/Home',Hod_View.Home,name='hod_home'),
    path('Hod/Student/Add',Hod_View.AddStudent,name="add_student"),
    path('Hod/Student/View', Hod_View.ViewStudent, name="view_student"),
    path('Hod/Student/Edit/<str:id>', Hod_View.EditStudent, name="edit_student"),
    path('Hod/Student/Update', Hod_View.UpdateStudent, name="update_student"),
    path('Hod/Student/Delete<str:admin>', Hod_View.DeleteStudent, name="delete_student"),

    path('Hod/Course/Add',Hod_View.AddCourse,name='add_course'),
    path('Hod/Course/View',Hod_View.ViewCourse,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_View.EditCourse,name='edit_course'),
    path('Hod/Course/Update', Hod_View.UpdateCourse, name='update_course'),
    path('Hod/Course/Delete<str:id>', Hod_View.DeleteCourse, name='delete_course'),

    path('Hod/Staff/Add',Hod_View.AddStaff,name="add_staff"),
    path('Hod/Staff/View',Hod_View.ViewStaff,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_View.EditStaff, name='edit_staff'),
    path('Hod/Staff/Update', Hod_View.UpdateStaff, name='update_staff'),
    path('Hod/Staff/Delete<str:admin>', Hod_View.DeleteStaff, name='delete_staff'),

    path('Hod/Subject/Add', Hod_View.AddSubject, name='add_subject'),
    path('Hod/Subject/View', Hod_View.ViewSubject, name='view_subject'),
    path('Hod/Subject/Edit/<str:id>', Hod_View.EditSubject, name='edit_subject'),
    path('Hod/Subject/Update', Hod_View.UpdateSubject, name='update_subject'),
    path('Hod/Subject/Delete<str:id>', Hod_View.DeleteSubject, name='delete_subject'),


    path('Hod/Session/Add',Hod_View.AddSession,name = 'add_session'),
    path('Hod/Session/View',Hod_View.ViewSession,name = 'view_session'),
    path('Hod/Session/Edit/<str:id>', Hod_View.EditSession, name='edit_session'),
    path('Hod/Session/Update', Hod_View.UpdateSession, name='update_session'),
    path('Hod/Session/Delete<str:id>', Hod_View.DeleteSession, name='delete_session'),

    path('Hod/Staff/Send_Notification',Hod_View.Staff_Send_Notification,name="staff_send_notification"),
    path('Hod/Staff/Save_Notification',Hod_View.Staff_Save_Notification,name="staff_save_notification"),

    path('Hod/Student/Send_Notification',Hod_View.Student_Send_Notification,name="student_send_notification"),
    path('Hod/Student/Save_Notification',Hod_View.Student_Save_Notification,name="student_save_notification"),

    path('Hod/Staff/Leave_View', Hod_View.Staff_Leave_View, name="staff_save_leave_view"),
    path('Hod/Staff/ApproveLeave/<str:id>', Hod_View.StaffApproveLeave, name='staff_approve_leave'),
    path('Hod/Staff/DisApproveLeave/<str:id>', Hod_View.StaffDisApproveLeave, name='staff_dis_approve_leave'),

    path('Hod/Staff/Feedback',Hod_View.Staff_Feedback,name='staff_feedback_reply'),
    path('Hod/Staff/Feedback/Save', Hod_View.Staff_Feedback_Save, name='staff_feedback_reply_save'),
    path('Hod/Student/Feedback', Hod_View.Student_Feedback, name='student_feedback_reply'),
    path('Hod/Student/Feedback/Save', Hod_View.Student_Feedback_Save, name='student_feedback_reply_save'),

    #This is staff Url
    path('Staff/Home',Staff_Views.Home,name='staff_home'),
    path('Staff/Notifications', Staff_Views.Notifications, name='notifications'),
    path('Staff/MarkAsRead/<str:status>', Staff_Views.MarkAsRead, name='mark_as_read'),
    path('Staff/ApplyLeave', Staff_Views.ApplyLeave, name='staff_apply_leave'),
    path('Staff/ApplyLeaveSave', Staff_Views.ApplyLeaveSave, name='staff_apply_leave_save'),


    path('Staff/Feedback',Staff_Views.StaffFeedback, name='staff_feedback'),
    path('Staff/Feedback/Save', Staff_Views.StaffFeedbackSave, name='staff_feedback_save'),



    #This is student panel
    path('Student/Home',Student_Views.Home,name='student_home'),
    path('Student/Notifications', Student_Views.StudentNotifications, name='student_notifications'),
    path('Student/MarkAsDone/<str:status>', Student_Views.MarkAsDone, name='mark_as_done'),
    path('Student/Feedback',Student_Views.StudentFeedback, name='student_feedback'),
    path('Student/Feedback/Save', Student_Views.StudentFeedbackSave, name='student_feedback_save'),







]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


