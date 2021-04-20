from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lg),
    path('adm_home/', views.adm_home),

    path('sports_add/', views.adm_spots_Cat),
    path('sports_view/', views.adm_spots_Cat_view),
    path('sports_update/<str:id>', views.adm_spots_Cat_edit),
    path('sports_update_post/', views.adm_spots_Cat_post),
    path('sports_del/<str:id>', views.adm_sport_cat_del),

    path('noti_add/', views.adm_notif_add),
    path('noti_view/', views.adm_notif_view),
    path('noti_update/<str:id>', views.adm_noti_edit),
    path('noti_update_post/', views.adm_noti_post),
    path('noti_del/<str:id>', views.adm_noti_del),

    path('adm_student_view/', views.adm_student_view),
    path('adm_student_view_more/<str:id>', views.adm_stud_viewmore),

    path('adm_college_view/', views.adm_college_view),
    path('adm_college_view_more/<str:id>', views.adm_college_viewmore),
    path('adm_college_approve_reject/', views.adm_college_approve_reject),

    path('adm_careerexp_view/', views.adm_careerexp_view),
    path('adm_v_view_more/<str:id>', views.adm_careerexp_viewmore),
    path('adm_careerexp_approve_reject/', views.adm__careerexp_approve_reject),

    path('adm_evntorgr_view/', views.adm_eventorgr_view),
    path('adm_evntorgr_view_more/<str:id>', views.adm_eventorgr_viewmore),
    path('adm_evntorgr_approve_reject/', views.adm__eventorgr_approve_reject),

    path('clg_sign_up/', views.clg_signup),
    path('clg_home/', views.clg_home),

    path('clg_staff_add/', views.clg_staff_add),
    path('clg_staff_view/', views.clg_staff_view),
    path('clg_staff_edit/<str:id>',views.clg_staff_edit),
    path('clg_staff_edit_post/', views.clg_staff_edit_post),
    path('clg_staff_del/<str:id>',views.clg_staff_del),

    path('clg_student_add/', views.clg_student_add),
    path('clg_student_view/', views.clg_student_view),
    path('clg_student_edit/<str:id>', views.clg_student_edit),
    path('clg_student_edit_post/', views.clg_student_edit_post),
    path('clg_student_del/<str:id>', views.clg_student_del),

    path('clg_assign_phycaltrainr/',views.clg_assign_phycaltrainr),
    path('event_orgr_signup/', views.evnt_staff_add),

]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

