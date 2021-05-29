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
    path('clg_staff_edit/<str:id>', views.clg_staff_edit),
    path('clg_staff_edit_post/', views.clg_staff_edit_post),
    path('clg_staff_del/<str:id>', views.clg_staff_del),

    path('clg_student_add/', views.clg_student_add),
    path('clg_student_view/', views.clg_student_view),
    path('clg_student_edit/<str:id>', views.clg_student_edit),
    path('clg_student_edit_post/', views.clg_student_edit_post),
    path('clg_student_del/<str:id>', views.clg_student_del),

    path('clg_assign_phycaltrainr/', views.clg_assign_phycaltrainr),

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
    path('phy_assign_clgteam_std', views.phy_assign_clgteam_std),

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

    path('phy_motiv_add/', views.phy_motiv_add),

    path('phy_evnt_view/', views.phy_evnt_view),
    path('phy_msg_frm_nutn_view/', views.phy_msg_frm_nutn_view),

    path('nut_home/', views.nut_home),
    # path('nut_staff_view/', views.clg_staff_view),
    path('nut_staff_edit/', views.nut_staff_edit),
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
    # chat
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

    path('pub_home/', views.pub_home),
    path('pub_noti_view/', views.pub_notif_view),
    path('pub_college_view/', views.pub_college_view),
    path('phy_glry_add/', views.phy_glry_add),
    path('phy_glry_view/', views.phy_gal_view),
    path('phy_glry_del/<str:id>', views.phy_gal_del),

    path('pub_glry_view/', views.pub_gal_view),

    path('fet_chat_phy', views.chatload_phy),
    path('drviewmsg_phy/<str:receiverid>', views.drviewmsg_phy),
    path('chatview_phy/', views.chatview_phy),
    path('doctor_insert_chat_phy/<str:receiverid>/<str:msg>', views.doctor_insert_chat_phy),

    # chat_phy_carrior
    path('fet_chat_phy_usr', views.chatload_phy_usr),
    path('drviewmsg_phy_usr/<str:receiverid>', views.drviewmsg_phy_usr),
    path('chatview_phy_usr/', views.chatview_phy_usr),
    path('doctor_insert_chat_phy_usr/<str:receiverid>/<str:msg>', views.doctor_insert_chat_phy_usr),

    path('carrior_user_signup/', views.carrior_user_add),
    path('carrior_portfolio_view/', views.carrier_portfolio_view),
    path('carrior_home/', views.carrier_home),

    # chat with carrior_phy
    path('fet_chat_usr_phy', views.chatload_usr_phy),
    path('drviewmsg_usr_phy/<str:receiverid>', views.drviewmsg_usr_phy),
    path('chatview_usr_phy/', views.chatview_usr_phy),
    path('doctor_insert_chat_usr_phy/<str:receiverid>/<str:msg>', views.doctor_insert_chat_usr_phy),

    path('evnt_org_home/', views.event_home),
    path('evnt_org_evnt_add/', views.clg_evnt_add),
    path('evnt_org_evnt_view/', views.clg_evnt_view),
    path('evnt_org_evnt_update/<str:id>', views.clgadm_evnt_edit),
    path('evnt_org_evnt_update_post/', views.clg_evnt_post),
    path('evnt_org_evnt_del/<str:id>', views.clg_evnt_del),

    ###e3scrime
    path('nut_alloc_rept_view/', views.nut_alloc_rept_view),
    path('clg_paricipants/', views.clg_paricipants),

    path('clg_paricipants_acpt/', views.clg_paricipants_acpt),
    path('clg_paricipants_accept/<str:id>', views.clg_paricipants_accept),
    path('clg_paricipants_reject/<str:id>', views.clg_paricipants_reject),

    path('fet_chat_clg', views.chatload_clg),
    path('drviewmsg_clg/<str:receiverid>', views.drviewmsg_clg),
    path('chatview_clg/', views.chatview_clg),
    path('doctor_insert_chat_clg/<str:receiverid>/<str:msg>', views.doctor_insert_chat_clg),

    path("and_login/", views.user_login),
    path("and_profile/", views.user_view_profile),
    path("user_view_portifolio/", views.user_view_portifolio),
    path("portifolio_add/", views.portifolio_add),

    path("user_view_teammembrs/", views.user_view_teammembrs),
    path("usr_view_motivation/", views.usr_view_motivation),
    path("usr_view_notif/", views.usr_view_notif),
    path("usr_view_cmt_reply/", views.usr_view_cmt_reply),
    path("usr_add_cmt/", views.usr_add_cmt),

    path("usr_view_msg_from_nutrilst/", views.usr_view_msg_from_nutrilst),

    path("usr_view_college_evnt/", views.usr_view_college_evnt),
    path("usr_view_college_evnt_requst/", views.usr_view_college_evnt_requst),
    path("usr_view_college_evnt_sts/", views.usr_view_college_evnt_sts),

    path("usr_view_eorg_evnt/", views.usr_view_eorg_evnt),
    path("usr_view_eorg_evnt_requst/", views.usr_view_eorg_evnt_requst),
    path("usr_view_eorg_evnt_sts/", views.usr_view_eorg_evnt_sts),

    path("usr_view_staff_chat1/", views.usr_view_staff_chat1),
    path('usr_view_college_chat1/', views.usr_view_college_chat1),

    path("api_Sendmessage/", views.api_Sendmessage),
    path('api_Sendmessage_clg/', views.api_Sendmessage_clg),
    path("api_chatview/", views.api_chatview),
    path("api_chatview_clg/", views.api_chatview_clg),

    # jqry
    path("ttt/", views.ttt),
    path("ttt_sub/", views.ttt_sub),
    path("ttt_pst/", views.ttt_pst),
    # JQRY OVR

    # 4 SPRINT
    path('eorg_evnt_add/', views.eorg_evnt_add),
    path('eorg_evnt_view/', views.eorg_evnt_view),
    path('eorg_evnt_update/<str:id>', views.eorg_evnt_edit),
    path('eorg_evnt_update_post/', views.eorg_evnt_post),
    path('eorg_evnt_del/<str:id>', views.eorg_evnt_del),

    path('clg_cmt_view/', views.clg_cmt_view),
    path('clg_cmt_reply/<str:id>/<str:cmt>', views.clg_cmt_reply),
    path('clg_cmt_reply_post/', views.clg_cmt_preply_post),
    path('eorg_view_particint', views.eorg_view_particint),
    path('eorg_view_particint_approve/<str:id>', views.eorg_view_particint_approve),
    path('eorg_view_particint_reject/<str:id>', views.eorg_view_particint_reject),

    # chat with carrir_phy_nw
    path('fet_chat_phy_car', views.chatload_phy_car),
    path('drviewmsg_phy_car/<str:receiverid>', views.drviewmsg_phy_car),
    path('chatview_phy_car/', views.chatview_phy_car),
    path('doctor_insert_chat_phy_car/<str:receiverid>/<str:msg>', views.doctor_insert_chat_phy_car),

    path('fet_chat_phy_car_to', views.chatload_phy_car_to),
    path('drviewmsg_phy_car_to/<str:receiverid>', views.drviewmsg_phy_car_to),
    path('chatview_phy_car_to/', views.chatview_phy_car_to),
    path('doctor_insert_chat_phy_car_to/<str:receiverid>/<str:msg>', views.doctor_insert_chat_phy_car_to),

    path('clg_assign_view', views.clg_assign_view),
    path('clg_assign_del/<str:id>', views.clg_assign_del),
    path('clg_teammbr_view', views.clg_teammbr_view),
    path('clg_teambr_del/<str:id>', views.clg_teambr_del),

    path('org_paricipants/', views.org_paricipants),

    path('org_paricipants_acpt/', views.org_paricipants_acpt),
    path('org_paricipants_accept/<str:id>', views.org_paricipants_accept),
    path('org_paricipants_reject/<str:id>', views.org_paricipants_reject),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

