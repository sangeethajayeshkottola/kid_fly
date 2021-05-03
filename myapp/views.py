from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



from .models import loginmodel,studentmodel,collegemodel,chat,notificationmodel,sports_catmodel,sports_profilemodel,assign_cate_model,staffmodel,complaintmodel,collegeteammodel,schedulemodel,team_member_model,motivationmodel,participantmodel,usermodel,gallerymodel,nutritionmodel,eventmodel,nutritionallocationmodel,msg_nutitionnist_model,eventorgizermodel

def lg(request):
    if request.method=="POST":
        print("hai")


        a = request.POST["textfield"]
        b = request.POST["textfield2"]
        if loginmodel.objects.filter(uname=a, pwd=b).exists():
            yy=loginmodel.objects.get(uname=a, pwd=b)
            # request["lid"]=yy.id
            request.session["lid"] = yy.id
            if yy.type == "admin":

                return render(request, "home.html")
            if yy.type == "college":
                qq=collegemodel.objects.get(LID=yy.id)
                if qq.status=="approve":
                    print("ok")
                    return render(request, "college/home.html")
                else:
                    print("no")
                    return render(request, "login.html")


            if yy.type == "phy":

                return render(request, "physical/home.html")

            if yy.type == "nut":
                return render(request, "nutition/home.html")

            if yy.type == "carrier":

                return render(request, "carrier/home.html")
            if yy.type == "eventorg":
                qq = eventorgizermodel.objects.get(LID=yy.id)
                if qq.status == "approve":
                    print("ok")
                    return render(request, "event_orgizr/home.html")
                else:
                    print("no")
                    return render(request, "login.html")



            else:
                return HttpResponse("no values")

        else:
            print("no")

    return render(request, "login.html")


def adm_home(request):
    return render(request,"home.html")

def clg_home(request):
    return render(request,"college/home.html")


def adm_spots_Cat(request):

    if request.method == "POST":
        name22 = request.POST['sname']
        dis22=request.POST["dis"]
        a1 =sports_catmodel(name=name22,description=dis22)
        a1.save()



        return render(request, "home.html")
    return render(request, 'add_sports.html')


def adm_spots_Cat_view(request):

    res = sports_catmodel.objects.all()

    return render(request, "view_sports_category.html", {'res': res})

def adm_spots_Cat_edit(request,id):
    res = sports_catmodel.objects.get(id=id)
    request.session["id"]=id

    return render(request,'edit_sport_cat.html', {'res':res})

@csrf_exempt
def adm_spots_Cat_post(request):
    id =  request.session["id"]

    na1=request.POST["sname"]
    dis = request.POST["dis"]

    res = sports_catmodel.objects.get(id=id)

    if request.method == "POST":
        res.name=na1
        res.description=dis
        res.save()


        return render(request,"home.html")
    return render(request, 'edit_sport_cat.html', {'res': res})

def adm_sport_cat_del(request, id):
    res = sports_catmodel.objects.get(id=id)
    res.delete()
    return  render(request,"home.html")

################

def adm_notif_add(request):

    if request.method == "POST":
        msg = request.POST['textfield']
        type22="admin"
        import datetime
        yy=datetime.datetime.now().strftime("%Y-%m-%d")
        print("ss=",yy)
        a1 =notificationmodel(msg=msg,datee=yy,type=type22)
        a1.save()



        return render(request, "home.html")
    return render(request, 'Notification_add.html')


def adm_notif_view(request):

    res = notificationmodel.objects.all()

    return render(request, "View_notification.html", {'res': res})

def adm_noti_edit(request,id):
    res = notificationmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"]=id

    return render(request,'edit_notifi.html', {'res':res})

@csrf_exempt
def adm_noti_post(request):
    id =  request.session["id"]

    na1=request.POST["textfield"]


    res = notificationmodel.objects.get(id=id)

    if request.method == "POST":
        res.msg=na1
        # res.description=dis
        res.save()


        return render(request,"home.html")
    return render(request, 'edit_notifi.html', {'res': res})

def adm_noti_del(request, id):
    res = notificationmodel.objects.get(id=id)
    res.delete()
    return  render(request,"home.html")


def adm_student_view(request):
    if request.method == "POST":
        b = request.POST["ser"]
        print("jj")
        res = studentmodel.objects.filter(name__startswith=b)
    else:


        res = studentmodel.objects.all()

    return render(request, "vew_student_records.html", {'res': res})
def adm_stud_viewmore(request,id):
    try:
        print("entr")
        res = participantmodel.objects.get(id=id)
        print("res=",res)
        return render(request, 'stud_record_view_more.html', {'res': res})
    except:
        return HttpResponse("no values")




def adm_college_view(request):
    if request.method=="POST":
        b=request.POST["ser"]
        print("jj")
        res=collegemodel.objects.filter(name__startswith=b)
    else:


        res = collegemodel.objects.all()

    return render(request, "approve_college.html", {'res': res})
def adm_college_viewmore(request,id):
    res = collegemodel.objects.get(id=id)
    request.session["id"]=id

    return render(request,'approve_college_view_more.html', {'i':res})

def adm_college_approve_reject(request):

    if request.method == "POST":
        print("jk")
        msg = request.POST['btn']
        id22=request.session["id"]
        print("id=",id22)
        print("hlw")
        if msg=="Approve":
            res = collegemodel.objects.get(id=id22)

            res.status = 'approve'
                # res.description=dis
            res.save()
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            import smtplib
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("rissprjcalicut555@gmail.com", "P09388434043")
            msg = MIMEMultipart()  # create a message.........."
            message = "Account Verifiction"
            msg['From'] = "rissprjcalicut555@gmail.com"
            msg['To'] = res.email
            msg['Subject'] = "Account Verifiction"
            body = "Your Account approved:- - "
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)

            print("jjj2")
            # a1 =collegemodel.filter(id=id22).update(status='approve')
        else:
            res = collegemodel.objects.get(id=id22)

            res.status = 'reject'
            # res.description=dis
            res.save()

        return render(request, "home.html")


def adm_careerexp_view(request):
    if request.method == "POST":
        b = request.POST["ser"]
        print("jj")
        res = usermodel.objects.filter(utype__startswith=b)
    else:

        res = usermodel.objects.all()

    return render(request, "approve_other_users.html", {'res': res})
def adm_careerexp_viewmore(request,id):
    res = usermodel.objects.get(id=id)
    request.session["id"]=id

    return render(request,'approve_other_users_view_more.html', {'i':res})
def adm__careerexp_approve_reject(request):

    if request.method == "POST":
        msg = request.POST['btn']
        id22=request.session["id"]
        if msg=="Approve":
            print("jjj")
            res = usermodel.objects.get(id=id22)

            res.status = 'approve'
            # res.description=dis
            res.save()

            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            import smtplib
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("rissprjcalicut555@gmail.com", "P09388434043")
            msg = MIMEMultipart()  # create a message.........."
            message = "Account Verifiction"
            msg['From'] = "rissprjcalicut555@gmail.com"
            msg['To'] = res.email
            msg['Subject'] = "Account Verifiction"
            body = "Your Account approved:- - "
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)

        else:
            res = usermodel.objects.get(id=id22)

            res.status = 'reject'
            # res.description=dis
            res.save()

        return render(request, "home.html")



###########

def adm_eventorgr_view(request):
    if request.method == "POST":
        b = request.POST["ser"]
        print("jj")
        res = eventorgizermodel.objects.filter(name__startswith=b)
    else:

        res = eventorgizermodel.objects.all()

    return render(request, "approve_eventorgaizer.html", {'res': res})
def adm_eventorgr_viewmore(request,id):
    res = eventorgizermodel.objects.get(id=id)
    request.session["id"]=id

    return render(request,'approve_other_eventorgizr_view_more.html', {'i':res})
def adm__eventorgr_approve_reject(request):

    if request.method == "POST":
        msg = request.POST['btn']
        id22=request.session["id"]
        if msg=="Approve":
            print("jjj")
            res = eventorgizermodel.objects.get(id=id22)

            res.status = 'approve'
            # res.description=dis
            res.save()
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            import smtplib
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("rissprjcalicut555@gmail.com", "P09388434043")
            msg = MIMEMultipart()  # create a message.........."
            message = "Account Verifiction"
            msg['From'] = "rissprjcalicut555@gmail.com"
            msg['To'] = res.email
            msg['Subject'] = "Account Verifiction"
            body = "Your Account approved:- - "
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)



        else:
            res = eventorgizermodel.objects.get(id=id22)

            res.status = 'reject'
            # res.description=dis
            res.save()

        return render(request, "home.html")



#########




def clg_signup(request):

    if request.method == "POST":
        print("jj")
        name22 = request.POST['d_name']
        ext_year = request.POST['exp_year']
        place = request.POST['place']
        post = request.POST['post']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        email = request.POST['email']
        status="pending"


        upload_file = request.FILES['img']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/" + upload_file.name
        print("jj3")
        pwd22=request.POST['pwd']

        # import random
        # rr = random.randint(0000, 9999)
        b1 = loginmodel(uname=email, pwd=pwd22, type="college")
        b1.save()
        ab = loginmodel.objects.latest('id')
        print("ab=", ab.pk)

        mmss = loginmodel.objects.get(id=ab.pk)

        a1 = collegemodel(LID=mmss,name=name22,ext_year=ext_year,place=place,post=post,img=fs.url(name),city=city,state=state,phone=phone,email=email,status=status)
        a1.save()

        # import smtplib
        # from email.mime.multipart import MIMEMultipart
        # from email.mime.text import MIMEText
        # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # s.starttls()
        # s.login("riss.mridul@gmail.com", "rissstaff")
        # msg = MIMEMultipart()  # create a message.........."
        # message = "Messege txt"
        # msg['From'] = "riss.projects555@gmail.com"
        # msg['To'] = email
        # msg['Subject'] = "Your Password"
        # body = "Your Password is:- - " + str(rr)
        # msg.attach(MIMEText(body, 'plain'))
        # s.send_message(msg)
        # print("kkkkkk")




        return render(request, "login.html")

    return render(request, 'college/college_signup.html')


def clg_staff_add(request):

    if request.method == "POST":
        print("jj")
        name22 = request.POST['name']
        upload_file = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/stf/" + upload_file.name

        dob = request.POST['dob']
        place = request.POST['place']
        gen = request.POST['gen']
        print("qq")
        cid= request.session["lid"]
        print(cid)
        log_ob=loginmodel.objects.get(id=cid)
        mmss22 = collegemodel.objects.get(LID=log_ob)
        print(mmss22)
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        type=request.POST['ty']
        phone = request.POST['phone']
        email = request.POST['email']
        import random
        rr = random.randint(0000, 9999)
        #tst
        from datetime import datetime
        date_format = "%Y-%m-%d"
        start = datetime.strptime(dob, date_format)
        now = datetime.now()
        if now < start:
            print("ys")
            return HttpResponse("Please check Date")
        else:
            print("nn")

            if type == "nut":
                print("qq")
                b1 = loginmodel(uname=email, pwd=rr, type="nut")
                b1.save()
            elif type == "phy":
                b1 = loginmodel(uname=email, pwd=rr, type="phy")
                b1.save()

            ab = loginmodel.objects.latest('id')
            print("ab=", ab.pk)

            mmss = loginmodel.objects.get(id=ab.pk)

            a1 = staffmodel(LOGIN=mmss, name=name22, dob=dob, place=place, gen=gen, image=fs.url(name), COLLEGE=mmss22,
                            city=city, state=state, pin=pin, type=type, email=email, phone=phone)
            a1.save()

            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("rissprjcalicut555@gmail.com", "P09388434043")
            msg = MIMEMultipart()  # create a message.........."
            message = "New Passoword"
            msg['From'] = "rissprjcalicut555@gmail.com"
            msg['To'] = email
            msg['Subject'] = "Your Password"
            body = "Your Password is:- - " + str(rr)
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)
            print("kkkkkk")

        ##ovr

        #
        return render(request, "college/home.html")

    return render(request, 'college/Staff_add.html')


def clg_staff_view(request):
    if request.method=="POST":
        b=request.POST["ser"]
        print("jj")
        res=staffmodel.objects.filter(name__startswith=b)
    else:


        res = staffmodel.objects.all()

    return render(request, "college/staff_view.html", {'res': res})


def clg_staff_edit(request,id):
    res = staffmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"]=id

    return render(request,'college/staff_edit.html', {'res':res})

@csrf_exempt
def clg_staff_edit_post(request):
    print("qq")
    id =  request.session["id"]
    print("id=",id)

    name22 = request.POST['name']
    upload_file = request.FILES['image']
    fs = FileSystemStorage()
    name = fs.save(upload_file.name, upload_file)
    url = "/media/stf/" + upload_file.name
    dob = request.POST['dob']
    place = request.POST['place']
    gen = request.POST['gen']
    cid = request.session["lid"]
    print("cid=",cid)
    log_ob=loginmodel.objects.get(id=cid)
    mmss22 = collegemodel.objects.get(LID=cid)
    print(mmss22)

    city = request.POST['city']
    state = request.POST['state']
    pin = request.POST['pin']
    type = request.POST['ty']
    phone = request.POST['phone']
    email = request.POST['email']
    print("qq")
    import random
    rr = random.randint(0000, 9999)
    b1 = loginmodel(uname=email, pwd=rr, type="staff")
    b1.save()
    ab = loginmodel.objects.latest('id')
    print("ab=", ab.pk)

    mmss = loginmodel.objects.get(id=ab.pk)

    res = staffmodel.objects.get(id=id)

    if request.method == "POST":
        print("entr")
        res.name=name22
        res.image=fs.url(name)
        res.dob=dob
        res.place=place
        res.gen=gen
        res.city=city
        res.state=state
        res.pin=pin
        res.type=type
        res.phone=phone

        # res.description=dis
        res.save()


        return render(request,"college/home.html")
    return render(request, 'college/staff_edit.html', {'res': res})

def clg_staff_del(request, id):
    res = staffmodel.objects.get(id=id)
    res.delete()
    return  render(request,"college/home.html")
##########



def clg_student_add(request):

    if request.method == "POST":
        print("jj")
        name22 = request.POST['name']
        place = request.POST['place']
        upload_file = request.FILES['img']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/stf/" + upload_file.name
        house = request.POST['house']
        post = request.POST['post']
        cid=request.session["lid"]
        log_ob=loginmodel.objects.get(id=cid)
        mmss22 = collegemodel.objects.get(LID=log_ob)

        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']
        dob=request.POST['dob']
        department = request.POST['department']
        sem = request.POST['ty']
        print("qqq")
        gen22=request.POST['gen']
        print("sss")
        import random
        rr = random.randint(0000, 9999)
        b1 = loginmodel(uname=email, pwd=rr, type="student")
        b1.save()
        ab = loginmodel.objects.latest('id')
        print("ab=", ab.pk)

        mmss = loginmodel.objects.get(id=ab.pk)

        a1 = studentmodel(LID=mmss,name=name22,place=place,img=fs.url(name),house=house,post=post,COLLEGE=mmss22,city=city,email=email,phone=phone,dob=dob,department=department,sem=sem,gen=gen22)
        a1.save()


        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("rissprjcalicut555@gmail.com", "P09388434043")
        msg = MIMEMultipart()  # create a message.........."
        message = "New Passoword"
        msg['From'] = "rissprjcalicut555@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Password"
        body = "Your Password is:- - " + str(rr)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        print("kkkkkk")




        return render(request, "college/home.html")

    return render(request, 'college/student_add.html')


def clg_student_view(request):
    if request.method=="POST":
        b=request.POST["ser"]
        print("jj")
        res=studentmodel.objects.filter(name__startswith=b)
    else:


        res = studentmodel.objects.all()

    return render(request, "college/student_view.html", {'res': res})


def clg_student_edit(request,id):
    res = studentmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"]=id

    return render(request,'college/student_edit.html', {'res':res})

@csrf_exempt
def clg_student_edit_post(request):
    print("qqq")
    id =  request.session["id"]


    res = studentmodel.objects.get(id=id)

    name22 = request.POST['name']
    place = request.POST['place']
    upload_file = request.FILES['image']
    fs = FileSystemStorage()
    name = fs.save(upload_file.name, upload_file)
    url = "/media/stf/" + upload_file.name
    house = request.POST['house']
    post = request.POST['post']
    cid = request.session["lid"]
    lob_ob=loginmodel.objects.get(id=cid)
    mmss22 = collegemodel.objects.get(LID=lob_ob)
    print("qq")

    city = request.POST['city']
    email = request.POST['email']
    phone = request.POST['phone']
    dob = request.POST['dob']
    department = request.POST['department']
    sem = request.POST['ty']
    gen = request.POST['gen']

    if request.method == "POST":
        print("ent")
        res.name=name22
        res.img=fs.url(name)
        res.place=place
        res.house=house
        res.post=post
        res.city=city
        res.email=email
        res.phone=phone
        res.dob=dob
        res.department=department
        res.sem=sem
        res.gen=gen

        # res.description=dis
        res.save()


        return render(request,"college/home.html")
    return render(request, 'college/student_edit.html', {'res': res})

def clg_student_del(request, id):
    res = studentmodel.objects.get(id=id)
    res.delete()
    return  render(request,"college/home.html")



def clg_assign_phycaltrainr(request):

    if request.method == "POST":
        cid = request.POST["cid"]
        mmss = sports_catmodel.objects.get(id=cid)

        sid = request.POST["sid"]
        mmss2 = staffmodel.objects.get(id=sid)

        import datetime
        yy = datetime.datetime.now().strftime("%Y-%m-%d")
        print("ss=", yy)

        a1 =assign_cate_model(SPORTS_CATE=mmss,STAFF=mmss2,date=yy)
        a1.save()


        return render(request, "college/home.html")
    res = sports_catmodel.objects.all()
    ck=request.session["lid"]
    cm=collegemodel.objects.get(LID=ck)
    log_ob=loginmodel.objects.filter(type='phy')
    res2 = []
    for i in log_ob:
        print("entr")
        print(i)
        qq=i.id
        print("qq=",qq)
        log_obnew=loginmodel.objects.get(id=qq)
        print("qs")
        print(log_obnew)
        stf_new=staffmodel.objects.get(LOGIN=log_obnew)
        print(stf_new)
        print("qwe")
        s = {'id': stf_new.id, 'name': stf_new.name}
        res2.append(s)
        print("yyy")

    print("ovr")




    print(res2)


    return render(request, 'college/assign_sports_cate_staff.html',{'res':res,'res2':res2})


def evnt_staff_add(request):

    if request.method == "POST":
        print("jj")
        name22 = request.POST['name']
        upload_file = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/stf/" + upload_file.name
        ph = request.POST['phone']
        details = request.POST['details']

        desi= request.POST["desi"]
        status = "pending"
        email = request.POST['email']
        import random
        rr = random.randint(0000, 9999)
        b1 = loginmodel(uname=email, pwd=rr, type="eventorg")
        b1.save()
        ab = loginmodel.objects.latest('id')
        print("ab=", ab.pk)

        mmss = loginmodel.objects.get(id=ab.pk)

        a1 = eventorgizermodel(LOGIN=mmss,name=name22,ph=ph,details=details,image=fs.url(name),desi=desi,status=status,email=email)
        a1.save()

        # import smtplib
        # from email.mime.multipart import MIMEMultipart
        # from email.mime.text import MIMEText
        # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        # s.starttls()
        # s.login("riss.mridul@gmail.com", "rissstaff")
        # msg = MIMEMultipart()  # create a message.........."
        # message = "Messege txt"
        # msg['From'] = "riss.projects555@gmail.com"
        # msg['To'] = email
        # msg['Subject'] = "Your Password"
        # body = "Your Password is:- - " + str(rr)
        # msg.attach(MIMEText(body, 'plain'))
        # s.send_message(msg)
        # print("kkkkkk")




        return render(request, "login.html")

    return render(request, 'event_orgizr/event_org_signup.html')


###############

def clg_notif_add(request):

    if request.method == "POST":
        msg = request.POST['textfield']
        type22="clg"
        import datetime
        yy=datetime.datetime.now().strftime("%Y-%m-%d")
        print("ss=",yy)
        a1 =notificationmodel(msg=msg,datee=yy,type=type22)
        a1.save()



        return render(request, "college/home.html")
    return render(request, 'college/Notification_add.html')


def clg_adm_notif_view(request):

    res = notificationmodel.objects.all()

    return render(request, "college/View_notification.html", {'res': res})

def clgadm_noti_edit(request,id):
    res = notificationmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"]=id

    return render(request,'college/edit_notifi.html', {'res':res})

@csrf_exempt
def clg_adm_noti_post(request):
    id =  request.session["id"]

    na1=request.POST["textfield"]


    res = notificationmodel.objects.get(id=id)

    if request.method == "POST":
        res.msg=na1
        # res.description=dis
        res.save()


        return render(request,"college/home.html")
    return render(request, 'college/edit_notifi.html', {'res': res})

def clg_adm_noti_del(request, id):
    res = notificationmodel.objects.get(id=id)
    res.delete()
    return  render(request,"college/home.html")




def clg_college_profile(request):
    rr = request.session["lid"]
    kk=loginmodel.objects.get(id=rr)
    res=collegemodel.objects.get(LID=kk)

    return render(request,'college/View_profile.html', {'i':res})

def phy_assign_clgteam_std(request):

    if request.method == "POST":
        tm=request.POST["cid"]
        std=request.POST["sid"]
        s1=studentmodel.objects.get(id=std)
        t1=collegeteammodel.objects.get(id=tm)


        a1 =team_member_model(STUDENT=s1,TEAM=t1)
        a1.save()


        return render(request, "physical/home.html")
    print("h")
    cid = request.session["lid"]
    print("cid=",cid)
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)
    sidd=ms.COLLEGE.id
    clg_ob=collegemodel.objects.get(id=sidd)
    msk = collegeteammodel.objects.filter(COLLEGE=clg_ob)
    print(msk)
    print("uu")


    std = studentmodel.objects.filter(COLLEGE=clg_ob)
    print("ms")

    return render(request, 'physical/encroll_std_clg_team.html',{'res':msk,'res2':std})



def phy_traing_sch_Cat(request):

    if request.method == "POST":
        t1 = request.POST['time_from']
        t2=request.POST["time_to"]
        d1=request.POST["datee"]
        cid = request.POST["cid"]
        ob=collegeteammodel.objects.get(id=cid)

        a1 =schedulemodel(time_from=t1,time_to=t2,datee=d1,COLLEGETEAM=ob)
        a1.save()



        return render(request, "physical/home.html")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    msk = collegeteammodel.objects.filter(STAFF=ms)

    return render(request, 'physical/traing_sc_add.html',{'res':msk})


def phy_traing_sch_view(request):

    res = schedulemodel.objects.all()

    return render(request, "physical/train_sc_view.html", {'res': res})

def phy_traing_sch_edit(request,id):
    res = schedulemodel.objects.get(id=id)
    print(res)
    request.session["id"]=id

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    msk = collegeteammodel.objects.filter(STAFF=ms)


    return render(request,'physical/traing_sc_update.html', {'i':res,'res':msk})

@csrf_exempt
def phy_traing_sch_post(request):
    print("hhh")
    id =  request.session["id"]

    t1 = request.POST['time_from']
    t2 = request.POST["time_to"]
    d1 = request.POST["datee"]
    cid = request.POST["cid"]
    ob = collegeteammodel.objects.get(id=cid)

    res = schedulemodel.objects.get(id=id)

    if request.method == "POST":
        res.time_from=t1
        res.time_to=t2
        res.datee=d1
        res.COLLEGETEAM=ob
        res.save()


        return render(request,"physical/home.html")
    return render(request, 'physical/traing_sc_update.html', {'res': res})

def phy_traing_sch_del(request, id):
    res = schedulemodel.objects.get(id=id)
    res.delete()
    return  render(request,"physical/home.html")
####

def phy_sports_profile(request):

    if request.method == "POST":
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime = datetime.datetime.now()

        n1 = request.POST['name']
        p1 = request.POST["position"]
        d1 =showtime
        cid = request.POST["cid"]
        des= request.POST["des"]

        ob=studentmodel.objects.get(id=cid)

        a1 =sports_profilemodel(name=n1,position=p1,desc=des,date=d1,STUDENT=ob)
        a1.save()



        return render(request, "physical/home.html")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)
    clg_id=ms.COLLEGE.id

    clg_ob=collegemodel.objects.get(id=clg_id)
    print("ss")
    print(clg_ob)
    msk = studentmodel.objects.filter(COLLEGE=clg_ob)
    print(msk)

    return render(request, 'physical/sport_profile_add.html',{'res':msk})


def phy_sports_profile_view(request):

    res = sports_profilemodel.objects.all()

    return render(request, "physical/view_sprt_prfl_update.html", {'res': res})

def phy_sports_profile_edit(request,id):
    res = sports_profilemodel.objects.get(id=id)
    print(res)
    print("qqqq")
    request.session["id"] = id

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    clg_id = ms.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=clg_id)
    print(clg_ob)
    msk = studentmodel.objects.filter(COLLEGE=clg_ob)
    print(msk)

    return render(request, 'physical/sports_profile_update.html', {'i': res, 'res': msk})


@csrf_exempt
def phy_sports_profile_post(request):
    print("hhhh")
    id = request.session["id"]
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime = datetime.datetime.now()

    n1 = request.POST['name']
    p1 = request.POST["position"]
    d1 = showtime
    cid = request.POST["cid"]
    des = request.POST["des"]

    ob = studentmodel.objects.get(id=cid)

    res = sports_profilemodel.objects.get(id=id)
    print("rrr")

    if request.method == "POST":
        res.name = n1
        res.position = p1
        res.date = d1
        res.desc = des
        res.STUDENT = ob
        res.save()

        return render(request, "physical/home.html")
    return render(request, 'physical/sports_profile_update.html', {'res': res})


def phy_sports_profile_del(request, id):
    res = sports_profilemodel.objects.get(id=id)
    res.delete()
    return render(request, "physical/home.html")


def phy_motiv_add(request):

    if request.method == "POST":
        print("jj")
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime = datetime.datetime.now()

        date22=showtime
        # date22 = request.POST['date']
        ctype = request.POST['contnt_type']
        upload_file = request.FILES['path']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/fil/" + upload_file.name
        desci = request.POST['desci']

        cid=request.session["lid"]
        print("cid=",cid)
        log_ob=loginmodel.objects.get(id=cid)
        mmss22 = staffmodel.objects.get(LOGIN=log_ob)
        print(mmss22)

        a1 = motivationmodel(date=date22,contnt_type=ctype,path=fs.url(name),desci=desci,STAFF=mmss22)
        a1.save()



        return render(request, "physical/home.html")

    return render(request, 'physical/motiv_add.html')

def clg_evnt_add(request):

    if request.method == "POST":

        d1 = request.POST['date']
        e1 = request.POST['ename']
        des=request.POST['descri']
        etype=request.POST['etype']
        cid = request.session["lid"]
        log_ob=loginmodel.objects.get(id=cid)
        mmss22 = collegemodel.objects.get(LID=log_ob)

        a1 =eventmodel(date=d1,descri=des,etype=etype,COLLEGE=mmss22,ename=e1)
        a1.save()



        return render(request, "college/home.html")
    return render(request, 'college/event_add.html')


def clg_evnt_view(request):
    print("hlw")
    cid = request.session["lid"]
    print(cid)
    log_ob=loginmodel.objects.get(id=cid)
    mmss22 = collegemodel.objects.get(LID=log_ob)
    print(mmss22)

    res = eventmodel.objects.filter(COLLEGE=mmss22)
    print(res)

    return render(request, "college/event_view.html", {'res': res})

def clgadm_evnt_edit(request,id):
    res = eventmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"]=id

    return render(request,'college/event_edit.html', {'i':res})

@csrf_exempt
def clg_evnt_post(request):
    id=request.session["id"]
    d1 = request.POST['date']
    e1=request.POST['ename']
    des = request.POST['descri']
    etype = request.POST['etype']
    cid = request.session["lid"]
    log_ob=loginmodel.objects.get(id=cid)
    mmss22 = collegemodel.objects.get(LID=log_ob)

    res = eventmodel.objects.get(id=id)

    if request.method == "POST":
        res.date=d1
        res.descri=des
        res.etype=etype
        res.COLLEGE=mmss22
        res.ename=e1
        # res.description=dis
        res.save()


        return render(request,"college/home.html")
    return render(request, 'college/event_edit.html', {'res': res})

def clg_evnt_del(request, id):
    res = eventmodel.objects.get(id=id)
    res.delete()
    return  render(request,"college/home.html")



def phy_evnt_view(request):
    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    clg_id = ms.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=clg_id)

    res = eventmodel.objects.filter(COLLEGE=clg_ob)

    return render(request, "physical/event_view.html", {'res': res})



def phy_msg_frm_nutn_view(request):
    print("hlw")
    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)
    clg_id = ms.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=clg_id)
    print(clg_ob)

    clg_ob = collegemodel.objects.get(id=clg_id)
    print("kk")
    kk = nutritionmodel.objects.filter(CLG=clg_ob)
    print(kk)

    res2 = []
    for i in kk:
        print("entr")
        print(i)
        qq = i.id
        print("qq=", qq)
        nut_obnew = nutritionmodel.objects.get(id=qq)
        print("qs")
        print(nut_obnew)
        print("qrs")
        try:
            print("*******************************************")
            rk = msg_nutitionnist_model.objects.get(NUTRITION=nut_obnew)
            print(rk)
            print("yp")
            print(rk.id, rk.msg, rk.datee, rk.mtype, rk.NUTRITION.name)
            s = {'pk': rk.id, 'msg': rk.msg, 'datee': rk.datee, 'mtype': rk.mtype, 'nname': rk.NUTRITION.name
                 }
            res2.append(s)
        except:
            print("no valeee===========")
            # print(log_obnew)
            # stf_new = staffmodel.objects.get(LOGIN=log_obnew)
            # print(stf_new)
            # print("qwe")

    print("loop finish")
    print(res2)
    print("ovr")
    # return HttpResponse("jjj")



    # res = nutritionmodel.objects.get(CLG=clg_ob)
    # print("jjj")
    # print(res)
    # KK=msg_nutitionnist_model.objects.filter(NUTRITION=res)
    #
    return render(request, "physical/msg_View_nutr.html", {'res': res2})


def nut_home(request):

    return render(request, "nutition/home.html")

def nut_staff_view(request):
    lid=request.session["lid"]
    log_ob=loginmodel.objects.get(pk=lid)

    res = staffmodel.objects.get(LOGIN=log_ob)

    return render(request, "nutition/view profile.html", {'res': res})


def nut_staff_edit(request):
    lid = request.session["lid"]
    log_ob = loginmodel.objects.get(pk=lid)
    res = staffmodel.objects.get(LOGIN=log_ob)

    print(res)
    print("qq")
    # request.session["id"]=id

    return render(request,'nutition/edit_nutrn.html', {'res':res})

@csrf_exempt
def nut_staff_edit_post(request):
    print("qq")
    lid = request.session["lid"]
    log_ob = loginmodel.objects.get(pk=lid)
    res55 = staffmodel.objects.get(LOGIN=log_ob)
    print(res55)

    id =  res55

    name22 = request.POST['name']
    upload_file = request.FILES['image']
    fs = FileSystemStorage()
    name = fs.save(upload_file.name, upload_file)
    url = "/media/stf/" + upload_file.name
    dob = request.POST['dob']
    place = request.POST['place']
    gen = request.POST['gen']
    cid = res55.COLLEGE.id
    mmss22 = collegemodel.objects.get(id=cid)
    print(mmss22)
    city = request.POST['city']
    state = request.POST['state']
    pin = request.POST['pin']
    phone = request.POST['phone']
    email = request.POST['email']
    # import random
    # rr = random.randint(0000, 9999)
    # b1 = loginmodel(uname=email, pwd=rr, type="staff")
    # b1.save()
    # ab = loginmodel.objects.latest('id')
    # print("ab=", ab.pk)

    # mmss = loginmodel.objects.get(id=ab.pk)

    res = staffmodel.objects.get(id=res55.id)

    if request.method == "POST":
        res.name=name22
        res.image=fs.url(name)
        res.dob=dob
        res.place=place
        res.gen=gen
        res.city=city
        res.state=state
        res.pin=pin
        res.type='nut'
        res.phone=phone

        # res.description=dis
        res.save()


        return render(request,"nutition/home.html")
    return render(request, 'nutition/edit_nutrn.html', {'res': res})

# def nut_staff_del(request, id):
#     res = staffmodel.objects.get(id=id)
#     res.delete()
#     return  render(request,"nutition/home.html")


def nut_add(request):

    if request.method == "POST":
        n1 = request.POST['name']
        p1 = request.POST["descri"]
        lid=request.session["lid"]
        li_ob=loginmodel.objects.get(id=lid)
        st_ob=staffmodel.objects.get(LOGIN=li_ob)
        print("jjj")

        ob=st_ob.COLLEGE.id
        clg_ob=collegemodel.objects.get(id=ob)
        print("hlw")
        print(clg_ob)

        a1 =nutritionmodel(name=n1,descri=p1,CLG=clg_ob)
        a1.save()



        return render(request, "nutition/home.html")


    return render(request, 'nutition/nut_add.html')


def nut_view(request):
    lid = request.session["lid"]
    li_ob = loginmodel.objects.get(id=lid)
    st_ob = staffmodel.objects.get(LOGIN=li_ob)

    ob = st_ob.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=ob)

    res = nutritionmodel.objects.filter(CLG=clg_ob)

    return render(request, "nutition/view_nutrition.html", {'res': res})

def nut_edit(request,id):
    res = nutritionmodel.objects.get(id=id)
    request.session["id"]=id

    # cid = request.POST["lid"]
    # mmss = loginmodel.objects.get(id=cid)
    # ms = staffmodel.objects.get(LOGIN=mmss)
    # clg_id = ms.COLLEGE.id
    # clg_ob = collegeteammodel.objects.get(id=clg_id)
    #
    return render(request,'nutition/nut_edit.html', {'i':res})

@csrf_exempt
def nut_post(request):
    id22 =  request.session["id"]

    n1 = request.POST['name']
    p1 = request.POST["descri"]
    lid = request.session["lid"]
    li_ob = loginmodel.objects.get(id=lid)
    st_ob = staffmodel.objects.get(LOGIN=li_ob)

    ob = st_ob.COLLEGE.id
    clg_ob=collegemodel.objects.get(id=ob)

    res = nutritionmodel.objects.get(id=id22)

    if request.method == "POST":
        res.name=n1
        res.descri=p1
        res.CLG=clg_ob
        res.save()


        return render(request,"nutition/home.html")
    return render(request, 'nutition/nut_edit.html', {'res': res})

def nut_del(request, id):
    res = nutritionmodel.objects.get(id=id)
    res.delete()
    return  render(request,"nutition/home.html")



def nut_allo_add(request):

    if request.method == "POST":
        q1 = request.POST['quantity']
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime = datetime.datetime.now()

        d1 = showtime
        nid = request.POST["nid"]
        studid= request.POST["cid"]
        nu_ob=nutritionmodel.objects.get(id=nid)

        ob=studentmodel.objects.get(id=studid)

        a1 =nutritionallocationmodel(quantity=q1,datee=d1,NUTRITION=nu_ob,STUDENT=ob)
        a1.save()



        return render(request, "nutition/home.html")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    clg_id=ms.COLLEGE.id
    clg_ob=collegemodel.objects.get(id=clg_id)
    print(clg_ob)
    msk = studentmodel.objects.filter(COLLEGE=clg_ob)
    print("ss")
    print(msk)
    msk2=nutritionmodel.objects.filter(CLG=clg_ob)

    return render(request, 'nutition/nutrion_allocn_add.html',{'res':msk,'res2':msk2})


def nut_alloc_view(request):
    print("hhh")
    print("hhh")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)
    clg_id = ms.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=clg_id)
    print(clg_ob)
    kk = nutritionmodel.objects.filter(CLG=clg_ob)
    print(kk)

    res2 = []
    for i in kk:
        print("entr")
        print(i)
        qq = i.id
        print("qq=", qq)
        nut_obnew = nutritionmodel.objects.get(id=qq)
        print("qs")
        print(nut_obnew)
        print("qrs")
        try:
            print("new entr")
            rk = nutritionallocationmodel.objects.get(NUTRITION=nut_obnew)
            print("yp")
            print(rk)
            s = {'pk': rk.id, 'quantity': rk.quantity, 'datee': rk.datee, 'nname': rk.NUTRITION.name,
                 'sname': rk.STUDENT.name}
            res2.append(s)
        except:
            print("qqq22")
        # print(log_obnew)
        # stf_new = staffmodel.objects.get(LOGIN=log_obnew)
        # print(stf_new)
        # print("qwe")

        print("yyy")
    print(res2)
    print("ovr")
    # return HttpResponse("jjj")







    # res = nutritionallocationmodel.objects.filter(NUTRITION=kk)
    # print(res)
    #
    #
    return render(request, "nutition/nut_allo_view.html", {'res': res2})


def nut_alloc_del(request, id):
    res = nutritionallocationmodel.objects.get(id=id)
    res.delete()
    return  render(request,"nutition/home.html")



def chatload(request):
    return render(request,'nutition/fur_chat.html')

def drviewmsg(request,receiverid):

    doclidlid=request.session["lid"]
    print("!!!!!!!!!!",doclidlid,receiverid)
    log_ob=loginmodel.objects.get(id=doclidlid)
    doc=staffmodel.objects.get(LOGIN=log_ob)
    print(doc)
    # stud_ob=studentmodel.objects.get(LID=rec)
    xx=studentmodel.objects.get(id=receiverid)
    print(xx)
    obj=chat.objects.filter(FID=doc,UID=xx)
    print(obj)
    user_data=studentmodel.objects.get(id=receiverid)
    print(user_data)
    print("********************",obj)

    res = []
    for i in obj:
        s = {'id':i.pk, 'date':i.date,'msg':i.message,'type':i.type}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res,'name':user_data.name,'image':user_data.img})

def chatview(request):
    print("hai")
    cid = request.session["lid"]
    print(cid)
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)
    clg_id = ms.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=clg_id)
    print(clg_ob)
    da =studentmodel.objects.filter(COLLEGE=clg_ob)
    print(da)
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.name, 'email': i.email,'image':i.img}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})
def doctor_insert_chat(request,receiverid,msg):
    print("hai riss")

    dlid= request.session["lid"]
    log_ob=loginmodel.objects.get(id=dlid)
    dobj=staffmodel.objects.get(LOGIN=log_ob)
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime=datetime.datetime.now()
    print("qqq")

    obj=chat()
    obj.UID=studentmodel.objects.get(pk=receiverid)
    obj.FID=dobj
    obj.message=msg
    obj.type='fuser'
    obj.date=showtime
    obj.save()
    print("yyy")
    return JsonResponse({'status':'ok'})


def api_Sendmessage(request):
    print("ppppp")
    if request.method=="POST":
        print("ss")
        ulid= request.POST["from_id"]
        did= request.POST["to_id"]
        msgs=request.POST["message"]
        print("yyy")
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime=datetime.datetime.now()
        msg=chat()
        msg.NID=studentmodel.objects.get(LOGIN=loginmodel.objects.get(pk=ulid))
        msg.FID=studentmodel.objects.get(pk=did)
        msg.message=msgs
        msg.date=showtime
        msg.type="nuser"
        msg.save()

        return JsonResponse({'status':'ok'})


def api_chatview(request):
    if request.method == "POST":
        ulid = request.POST["ulid"]
        did = request.POST["did"]
        lastmid= request.POST["lastid"]

        print("lst=",lastmid)

        usr= studentmodel.objects.get(LOGIN=loginmodel.objects.get(pk=ulid))
        dctr= staffmodel.objects.get(pk=did)

        cha= chat.objects.filter(NID=usr,FID=dctr,pk__gt=lastmid)

        if cha.exists():
            a=[]
            for i in cha:
                a.append({'id':i.pk,'msg':i.message, 'date': i.date,'type':i.type})
            return JsonResponse({'status':'ok','data':a})
        else:
            return JsonResponse({'status':'no'})


def phy_team_add(request):

    if request.method == "POST":
        print("kk")
        t1 = request.POST['namee']
        import datetime
        yy = datetime.datetime.now().strftime("%Y-%m-%d")
        t2 = yy

        cid = request.session["lid"]
        print("oo")

        mmss = loginmodel.objects.get(id=cid)
        print(mmss)
        stf_ob = staffmodel.objects.get(LOGIN=mmss)
        print(stf_ob)
        clg_id=stf_ob.COLLEGE.id
        clg_ob = collegemodel.objects.get(id=clg_id)
        print(clg_ob)
        print("ww")

        a1 =collegeteammodel(namee=t1,datee=t2,STAFF=stf_ob,COLLEGE=clg_ob)
        a1.save()



        return render(request, "physical/home.html")



    return render(request, 'physical/Team_add.html')
def phy_home(request):
    return render(request, 'physical/home.html')


def phy_team_view(request):
    cid = request.session["lid"]

    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    stf_ob = staffmodel.objects.get(LOGIN=mmss)
    print(stf_ob)
    clg_id = stf_ob.COLLEGE.id
    print(clg_id)
    clg_ob = collegemodel.objects.get(id=clg_id)
    print(clg_ob.id)
    print("kk")

    res = collegeteammodel.objects.filter(COLLEGE=clg_ob)
    print("hj")


    return render(request, "physical/view_team.html", {'res': res})

def phy_team_edit(request,id):
    res = collegeteammodel.objects.get(id=id)
    request.session["id"]=id

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    msk = collegeteammodel.objects.get(STAFF=ms)


    return render(request,'physical/Team_edit.html', {'i':res})

@csrf_exempt
def phy_team_post(request):
    id =  request.session["id"]

    t1 = request.POST['namee']


    cid = request.session["lid"]

    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    stf_ob = staffmodel.objects.get(LOGIN=mmss)
    print(stf_ob)
    clg_id = stf_ob.COLLEGE.id
    print(clg_id)
    clg_ob = collegemodel.objects.get(id=clg_id)
    print(clg_ob.id)
    print("kk")

    res = collegeteammodel.objects.get(id=id)
    print("hj")

    import datetime
    yy = datetime.datetime.now().strftime("%Y-%m-%d")
    t2=yy
    print("hls")

    if request.method == "POST":
        res.namee=t1
        res.datee=t2
        res.COLLEGE=clg_ob
        res.STAFF=stf_ob
        res.save()


        return render(request,"physical/home.html")
    return render(request, 'physical/Team_edit.html', {'res': res})

def phy_team_del(request, id):
    res = collegeteammodel.objects.get(id=id)
    res.delete()
    return  render(request,"physical/home.html")

##

def nut_msg_add(request):

    if request.method == "POST":
        print("kk")
        t1 = request.POST['msg']
        t2=request.POST['mtype']
        nn=request.POST['nn']
        import datetime
        yy = datetime.datetime.now().strftime("%Y-%m-%d")
        t3 = yy
        nut_ob=nutritionmodel.objects.get(id=nn)


        a1 =msg_nutitionnist_model(msg=t1,datee=t3,mtype=t2,NUTRITION=nut_ob)
        a1.save()



        return render(request, "nutition/home.html")

    cid = request.session["lid"]
    print("oo")

    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    stf_ob = staffmodel.objects.get(LOGIN=mmss)
    print(stf_ob)
    clid=stf_ob.COLLEGE.id
    cl_ob=collegemodel.objects.get(id=clid)
    rrr=nutritionmodel.objects.filter(CLG=cl_ob)

    print("ww")

    return render(request, 'nutition/msg_add.html',{'res':rrr})




def nut_msg_view(request):
    print("entr")
    cid = request.session["lid"]
    print(cid)

    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    stf_ob = staffmodel.objects.get(LOGIN=mmss)
    print(stf_ob)
    clg_id = stf_ob.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=clg_id)
    print("kk")
    kk = nutritionmodel.objects.filter(CLG=clg_ob)
    print(kk)

    res2 = []
    for i in kk:
        print("entr")
        print(i)
        qq = i.id
        print("qq=", qq)
        nut_obnew = nutritionmodel.objects.get(id=qq)
        print("qs")
        print(nut_obnew)
        print("qrs")
        try:
            print("*******************************************")
            rk = msg_nutitionnist_model.objects.get(NUTRITION=nut_obnew)
            print(rk)
            print("yp")
            print(rk)
            s = {'pk': rk.id, 'msg': rk.msg, 'datee': rk.datee, 'mtype': rk.mtype
                 }
            res2.append(s)
        except:
            print("no valeee===========")
            # print(log_obnew)
            # stf_new = staffmodel.objects.get(LOGIN=log_obnew)
            # print(stf_new)
            # print("qwe")

    print("loop finish")
    print(res2)
    print("ovr")
    # return HttpResponse("jjj")


    # res = msg_nutitionnist_model.objects.filter(NUTRITION=nt)
    # print("hj")
    #
    #
    return render(request, "nutition/view_msg.html", {'res': res2})


def nut_msg_edit(request,id):
    res = msg_nutitionnist_model.objects.get(id=id)
    request.session["id"]=id

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)

    cid = request.session["lid"]
    print("oo")
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    stf_ob = staffmodel.objects.get(LOGIN=mmss)
    print(stf_ob)
    clid = stf_ob.COLLEGE.id
    cl_ob = collegemodel.objects.get(id=clid)
    rrr = nutritionmodel.objects.filter(CLG=cl_ob)

    print("ww")

    return render(request,'nutition/msg_edit.html', {'i':res,'rrr':rrr})

@csrf_exempt
def nut_msg_post(request):
    id =  request.session["id"]



    cid = request.session["lid"]

    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    stf_ob = staffmodel.objects.get(LOGIN=mmss)
    print(stf_ob)
    t1 = request.POST['msg']
    t2 = request.POST['mtype']
    nut=request.POST['nn']
    nut_ob=nutritionmodel.objects.get(id=nut)

    import datetime
    yy = datetime.datetime.now().strftime("%Y-%m-%d")
    t3 = yy

    res = msg_nutitionnist_model.objects.get(id=id)
    print("hj")



    if request.method == "POST":
        res.msg=t1
        res.datee=t3
        res.mtype=t2
        res.NUTRITION=nut_ob
        res.save()


        return render(request,"nutition/home.html")
    return render(request, 'nutition/msg_edit.html', {'res': res})

def nut_msg_del(request, id):
    res = msg_nutitionnist_model.objects.get(id=id)
    res.delete()
    return  render(request,"nutition/home.html")



def phy_categry_assigned_view(request):
    print("hhh")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)

    res = assign_cate_model.objects.filter(STAFF=ms)
    print(res)
    # res33=nutritionallocationmodel.objects.all()

    return render(request, "physical/view_category_assigned.html", {'res': res})


def phy_motiv_view(request):
    print("hhh")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)


    res = motivationmodel.objects.filter(STAFF=ms)
    print(res)
    # res33=nutritionallocationmodel.objects.all()

    return render(request, "physical/motiv_viw.html", {'res': res})

def phy_motiv_del(request, id):
    res = motivationmodel.objects.get(id=id)
    res.delete()
    return  render(request,"physical/home.html")

