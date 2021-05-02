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

    ################
path('clg_noti_add/', views.clg_notif_add),
    path('clg_noti_view/', views.clg_adm_notif_view),
    path('clg_noti_update/<str:id>', views.clgadm_noti_edit),
    path('clg_noti_update_post/', views.clg_adm_noti_post),
    path('clg_noti_del/<str:id>', views.clg_adm_noti_del),


path('clg_evnt_add/', views.clg_evnt_add),
    path('clg_evnt_view/', views.clg_evnt_view),
    path('clg_evnt_update/<str:id>', views.clgadm_evnt_edit),
    path('clg_evnt_update_post/', views.clg_evnt_post),
    path('clg_evnt_del/<str:id>', views.clg_evnt_del),


    path('clg_college_view_profile', views.clg_college_profile),
    path('phy_assign_clgteam_std',views.phy_assign_clgteam_std),

    path('phy_traing_sch_add/', views.phy_traing_sch_Cat),
    path('phy_traing_sch_view/', views.phy_traing_sch_view),
    path('phy_traing_sch_update/<str:id>', views.phy_traing_sch_edit),
    path('phy_traing_sch_update_post/', views.phy_traing_sch_post),
    path('phy_traing_sch_del/<str:id>', views.phy_traing_sch_del),

    path('phy_sports_profile_add/', views.phy_sports_profile),
    path('phy_sports_profile_view/', views.phy_sports_profile_view),
    path('phy_sports_profile_update/<str:id>', views.phy_sports_profile_edit),
    path('phy_sports_profile_update_post/', views.phy_sports_profile_post),
    path('phy_sports_profile_del/<str:id>', views.phy_sports_profile_del),

    path('phy_motiv_add/',views.phy_motiv_add),

    path('phy_evnt_view/', views.phy_evnt_view),
    path('phy_msg_frm_nutn_view/',views.phy_msg_frm_nutn_view),

    path('nut_home/', views.nut_home),
# path('nut_staff_view/', views.clg_staff_view),
    path('nut_staff_edit/',views.nut_staff_edit),
    path('nut_staff_edit_post/', views.nut_staff_edit_post),
    # path('nut_staff_del/<str:id>',views.clg_staff_del),

path('nut_add/', views.nut_add),
    path('nut_view/', views.nut_view),
    path('nut_update/<str:id>', views.nut_edit),
    path('nut_update_post/', views.nut_post),
    path('nut_del/<str:id>', views.nut_del),

    path('nut_alloc_add/', views.nut_allo_add),
    path('nut_alloc_view/', views.nut_alloc_view),
    path('nut_alloc_del/<str:id>', views.nut_alloc_del),
    #chat
    path('fet_chat', views.chatload),
    path('drviewmsg/<str:receiverid>', views.drviewmsg),
    path('chatview/', views.chatview),
    path('doctor_insert_chat/<str:receiverid>/<str:msg>', views.doctor_insert_chat),

    # path('and_fmem__view', views.and_fmem__view),
    path('api_Sendmessage/', views.api_Sendmessage, name='m70'),
    path('api_chatview/', views.api_chatview, name='m70'),

    path('phy_team_add/', views.phy_team_add),
    path('phy_team_view/', views.phy_team_view),
    path('phy_team_update/<str:id>', views.phy_team_edit),
    path('phy_team_update_post/', views.phy_team_post),
    path('phy_team_del/<str:id>', views.phy_team_del),
    path('phy_home/', views.phy_home),

    path('nut_msg_add/', views.nut_msg_add),
    path('nut_msg_view/', views.nut_msg_view),

    path('nut_msg_update/<str:id>', views.nut_msg_edit),
    path('nut_msg_update_post/', views.nut_msg_post),
    path('nut_msg_del/<str:id>', views.nut_msg_del),


    path('phy_categry_assigned_view/', views.phy_categry_assigned_view),

    path('phy_motiv_view/', views.phy_motiv_view),
    path('phy_motiv_del/<str:id>', views.phy_motiv_del),

]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

