from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt


from .models import loginmodel,studentmodel,collegemodel,chat,notificationmodel,sports_catmodel,sports_profilemodel,assign_cate_model,staffmodel,complaintmodel,collegeteammodel,schedulemodel,team_member_model,motivationmodel,participantmodel,usermodel,gallerymodel,nutritionmodel,eventmodel,nutritionallocationmodel,msg_nutitionnist_model,eventorgizermodel

def lg(request):
    if request.method=="POST":


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


            if yy.type == "physical":

                return render(request, "physical/home.html")

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
    ii=studentmodel.objects.get(id=id)
    print("hhh")
    res = participantmodel.objects.get(STUDENT=ii)
    print("qqq")
    # request.session["id"]=id

    return render(request,'stud_record_view_more.html', {'res':res})


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
        cid= request.session["lid"]

        mmss22 = collegemodel.objects.get(LID=cid)
        print("hlw")
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        type=request.POST['ty']
        phone = request.POST['phone']
        email = request.POST['email']
        import random
        rr = random.randint(0000, 9999)
        b1 = loginmodel(uname=email, pwd=rr, type="staff")
        b1.save()
        ab = loginmodel.objects.latest('id')
        print("ab=", ab.pk)

        mmss = loginmodel.objects.get(id=ab.pk)

        a1 = staffmodel(LOGIN=mmss,name=name22,dob=dob,place=place,gen=gen,image=fs.url(name),COLLEGE=mmss22,city=city,state=state,pin=pin,type=type,email=email,phone=phone)
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
    id =  request.session["id"]

    name22 = request.POST['name']
    upload_file = request.FILES['image']
    fs = FileSystemStorage()
    name = fs.save(upload_file.name, upload_file)
    url = "/media/stf/" + upload_file.name
    dob = request.POST['dob']
    place = request.POST['place']
    gen = request.POST['gen']
    cid = request.session["lid"]
    mmss22 = collegemodel.objects.get(LID=cid)
    city = request.POST['city']
    state = request.POST['state']
    pin = request.POST['pin']
    type = request.POST['ty']
    phone = request.POST['phone']
    email = request.POST['email']
    import random
    rr = random.randint(0000, 9999)
    b1 = loginmodel(uname=email, pwd=rr, type="staff")
    b1.save()
    ab = loginmodel.objects.latest('id')
    print("ab=", ab.pk)

    mmss = loginmodel.objects.get(id=ab.pk)

    res = staffmodel.objects.get(id=id)

    if request.method == "POST":
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
        mmss22 = collegemodel.objects.get(LID=cid)

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
    mmss22 = collegemodel.objects.get(LID=cid)

    city = request.POST['city']
    email = request.POST['email']
    phone = request.POST['phone']
    dob = request.POST['dob']
    department = request.POST['department']
    sem = request.POST['ty']
    gen = request.POST['gen']

    if request.method == "POST":
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
    res2 = staffmodel.objects.filter(COLLEGE=cm)

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
