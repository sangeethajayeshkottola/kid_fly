from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import chat_staff_phy, complaintmodel, chat, chat_staff, participantmodel2, event2model, portfoliomodel, \
    loginmodel, studentmodel, collegemodel, notificationmodel, sports_catmodel, sports_profilemodel, assign_cate_model, \
    staffmodel, complaintmodel, collegeteammodel, schedulemodel, team_member_model, motivationmodel, participantmodel, \
    usermodel, gallerymodel, nutritionmodel, eventmodel, nutritionallocationmodel, msg_nutitionnist_model, \
    eventorgizermodel


def lg(request):
    if request.method == "POST":
        print("hai")

        a = request.POST["textfield"]
        b = request.POST["textfield2"]
        if loginmodel.objects.filter(uname=a, pwd=b).exists():
            yy = loginmodel.objects.get(uname=a, pwd=b)
            # request["lid"]=yy.id
            request.session["lid"] = yy.id
            if yy.type == "admin":
                return render(request, "home.html")
            if yy.type == "college":
                qq = collegemodel.objects.get(LID=yy.id)
                if qq.status == "approve":
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
                qq = eventorgizermodel.objects.get(LOGIN=yy.id)
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
    return render(request, "home.html")


def clg_home(request):
    return render(request, "college/home.html")


def adm_spots_Cat(request):
    if request.method == "POST":
        name22 = request.POST['sname']
        dis22 = request.POST["dis"]
        a1 = sports_catmodel(name=name22, description=dis22)
        a1.save()

        return render(request, "home.html")
    return render(request, 'add_sports.html')


def adm_spots_Cat_view(request):
    res = sports_catmodel.objects.all()

    return render(request, "view_sports_category.html", {'res': res})


def adm_spots_Cat_edit(request, id):
    res = sports_catmodel.objects.get(id=id)
    request.session["id"] = id

    return render(request, 'edit_sport_cat.html', {'res': res})


@csrf_exempt
def adm_spots_Cat_post(request):
    id = request.session["id"]

    na1 = request.POST["sname"]
    dis = request.POST["dis"]

    res = sports_catmodel.objects.get(id=id)

    if request.method == "POST":
        res.name = na1
        res.description = dis
        res.save()

        return render(request, "home.html")
    return render(request, 'edit_sport_cat.html', {'res': res})


def adm_sport_cat_del(request, id):
    res = sports_catmodel.objects.get(id=id)
    res.delete()
    return render(request, "home.html")


################

def adm_notif_add(request):
    if request.method == "POST":
        msg = request.POST['textfield']
        type22 = "admin"
        import datetime
        yy = datetime.datetime.now().strftime("%Y-%m-%d")
        print("ss=", yy)
        a1 = notificationmodel(msg=msg, datee=yy, type=type22)
        a1.save()

        return render(request, "home.html")
    return render(request, 'Notification_add.html')


def adm_notif_view(request):
    res = notificationmodel.objects.all()

    return render(request, "View_notification.html", {'res': res})


def adm_noti_edit(request, id):
    res = notificationmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"] = id

    return render(request, 'edit_notifi.html', {'res': res})


@csrf_exempt
def adm_noti_post(request):
    id = request.session["id"]

    na1 = request.POST["textfield"]

    res = notificationmodel.objects.get(id=id)

    if request.method == "POST":
        res.msg = na1
        # res.description=dis
        res.save()

        return render(request, "home.html")
    return render(request, 'edit_notifi.html', {'res': res})


def adm_noti_del(request, id):
    res = notificationmodel.objects.get(id=id)
    res.delete()
    return render(request, "home.html")


def adm_student_view(request):
    if request.method == "POST":
        b = request.POST["ser"]
        print("jj")
        res = studentmodel.objects.filter(name__startswith=b)
    else:

        res = studentmodel.objects.all()

    return render(request, "vew_student_records.html", {'res': res})


def adm_stud_viewmore(request, id):
    try:
        print("entr")
        res = participantmodel.objects.get(id=id)
        print("res=", res)
        return render(request, 'stud_record_view_more.html', {'res': res})
    except:
        return HttpResponse("no values")


def adm_college_view(request):
    if request.method == "POST":
        b = request.POST["ser"]
        print("jj")
        res = collegemodel.objects.filter(name__startswith=b)
    else:

        res = collegemodel.objects.all()

    return render(request, "approve_college.html", {'res': res})


def adm_college_viewmore(request, id):
    res = collegemodel.objects.get(id=id)
    request.session["id"] = id

    return render(request, 'approve_college_view_more.html', {'i': res})


def adm_college_approve_reject(request):
    if request.method == "POST":
        print("jk")
        msg = request.POST['btn']
        id22 = request.session["id"]
        print("id=", id22)
        print("hlw")
        if msg == "Approve":
            res = collegemodel.objects.get(id=id22)

            res.status = 'approve'
            # res.description=dis
            res.save()
            # import smtplib
            # from email.mime.multipart import MIMEMultipart
            # from email.mime.text import MIMEText
            #
            # import smtplib
            # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            # s.starttls()
            # s.login("rissprjcalicut555@gmail.com", "P09388434043")
            # msg = MIMEMultipart()  # create a message.........."
            # message = "Account Verifiction"
            # msg['From'] = "rissprjcalicut555@gmail.com"
            # msg['To'] = res.email
            # msg['Subject'] = "Account Verifiction"
            # body = "Your Account approved:- - "
            # msg.attach(MIMEText(body, 'plain'))
            # s.send_message(msg)

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


def adm_careerexp_viewmore(request, id):
    res = usermodel.objects.get(id=id)
    request.session["id"] = id

    return render(request, 'approve_other_users_view_more.html', {'i': res})


def adm__careerexp_approve_reject(request):
    if request.method == "POST":
        msg = request.POST['btn']
        id22 = request.session["id"]
        if msg == "Approve":
            print("jjj")
            res = usermodel.objects.get(id=id22)

            res.status = 'approve'
            # res.description=dis
            res.save()

            # import smtplib
            # from email.mime.multipart import MIMEMultipart
            # from email.mime.text import MIMEText
            #
            # import smtplib
            # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            # s.starttls()
            # s.login("rissprjcalicut555@gmail.com", "P09388434043")
            # msg = MIMEMultipart()  # create a message.........."
            # message = "Account Verifiction"
            # msg['From'] = "rissprjcalicut555@gmail.com"
            # msg['To'] = res.email
            # msg['Subject'] = "Account Verifiction"
            # body = "Your Account approved:- - "
            # msg.attach(MIMEText(body, 'plain'))
            # s.send_message(msg)

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


def adm_eventorgr_viewmore(request, id):
    res = eventorgizermodel.objects.get(id=id)
    request.session["id"] = id

    return render(request, 'approve_other_eventorgizr_view_more.html', {'i': res})


def adm__eventorgr_approve_reject(request):
    if request.method == "POST":
        msg = request.POST['btn']
        id22 = request.session["id"]
        if msg == "Approve":
            print("jjj")
            res = eventorgizermodel.objects.get(id=id22)

            res.status = 'approve'
            # res.description=dis
            res.save()
            # import smtplib
            # from email.mime.multipart import MIMEMultipart
            # from email.mime.text import MIMEText
            #
            # import smtplib
            # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            # s.starttls()
            # s.login("rissprjcalicut555@gmail.com", "P09388434043")
            # msg = MIMEMultipart()  # create a message.........."
            # message = "Account Verifiction"
            # msg['From'] = "rissprjcalicut555@gmail.com"
            # msg['To'] = res.email
            # msg['Subject'] = "Account Verifiction"
            # body = "Your Account approved:- - "
            # msg.attach(MIMEText(body, 'plain'))
            # s.send_message(msg)
            #


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
        status = "pending"

        upload_file = request.FILES['img']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/" + upload_file.name
        print("jj3")
        pwd22 = request.POST['pwd']

        # import random
        # rr = random.randint(0000, 9999)
        b1 = loginmodel(uname=email, pwd=pwd22, type="college")
        b1.save()
        ab = loginmodel.objects.latest('id')
        print("ab=", ab.pk)

        mmss = loginmodel.objects.get(id=ab.pk)

        a1 = collegemodel(LID=mmss, name=name22, ext_year=ext_year, place=place, post=post, img=fs.url(name), city=city,
                          state=state, phone=phone, email=email, status=status)
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
        cid = request.session["lid"]
        print(cid)
        log_ob = loginmodel.objects.get(id=cid)
        mmss22 = collegemodel.objects.get(LID=log_ob)
        print(mmss22)
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        type = request.POST['ty']
        phone = request.POST['phone']
        email = request.POST['email']
        import random
        rr = random.randint(0000, 9999)
        # tst
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

            # import smtplib
            # from email.mime.multipart import MIMEMultipart
            # from email.mime.text import MIMEText
            # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            # s.starttls()
            # s.login("rissprjcalicut555@gmail.com", "P09388434043")
            # msg = MIMEMultipart()  # create a message.........."
            # message = "New Passoword"
            # msg['From'] = "rissprjcalicut555@gmail.com"
            # msg['To'] = email
            # msg['Subject'] = "Your Password"
            # body = "Your Password is:- - " + str(rr)
            # msg.attach(MIMEText(body, 'plain'))
            # s.send_message(msg)
            print("kkkkkk")

        ##ovr

        #
        return render(request, "college/home.html")

    return render(request, 'college/Staff_add.html')


def clg_staff_view(request):
    if request.method == "POST":
        b = request.POST["ser"]
        print("jj")
        res = staffmodel.objects.filter(name__startswith=b)
    else:

        res = staffmodel.objects.all()

    return render(request, "college/staff_view.html", {'res': res})


def clg_staff_edit(request, id):
    res = staffmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"] = id

    return render(request, 'college/staff_edit.html', {'res': res})


@csrf_exempt
def clg_staff_edit_post(request):
    print("qq")
    id = request.session["id"]
    print("id=", id)

    name22 = request.POST['name']
    upload_file = request.FILES['image']
    fs = FileSystemStorage()
    name = fs.save(upload_file.name, upload_file)
    url = "/media/stf/" + upload_file.name
    dob = request.POST['dob']
    place = request.POST['place']
    gen = request.POST['gen']
    cid = request.session["lid"]
    print("cid=", cid)
    log_ob = loginmodel.objects.get(id=cid)
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
        from datetime import datetime
        date_format = "%Y-%m-%d"
        start = datetime.strptime(dob, date_format)
        now = datetime.now()
        if now < start:
            print("ys")
            return HttpResponse("Please check Date")
        else:
            print("nn")

            res.name = name22
            res.image = fs.url(name)
            res.dob = dob
            res.place = place
            res.gen = gen
            res.city = city
            res.state = state
            res.pin = pin
            res.type = type
            res.phone = phone

            # res.description=dis
            res.save()

            return render(request, "college/home.html")
    return render(request, 'college/staff_edit.html', {'res': res})


def clg_staff_del(request, id):
    res = staffmodel.objects.get(id=id)
    res.delete()
    return render(request, "college/home.html")


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
        cid = request.session["lid"]
        log_ob = loginmodel.objects.get(id=cid)
        mmss22 = collegemodel.objects.get(LID=log_ob)

        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        department = request.POST['department']
        sem = request.POST['ty']
        print("qqq")
        gen22 = request.POST['gen']
        print("sss")
        import random
        rr = random.randint(0000, 9999)
        # tst
        from datetime import datetime
        date_format = "%Y-%m-%d"
        start = datetime.strptime(dob, date_format)
        now = datetime.now()
        if now < start:
            print("ys")
            return HttpResponse("Please check Date")
        else:
            print("nn")

            b1 = loginmodel(uname=email, pwd=rr, type="student")
            b1.save()
            ab = loginmodel.objects.latest('id')
            print("ab=", ab.pk)

            mmss = loginmodel.objects.get(id=ab.pk)

            a1 = studentmodel(LID=mmss, name=name22, place=place, img=fs.url(name), house=house, post=post,
                              COLLEGE=mmss22, city=city, email=email, phone=phone, dob=dob, department=department,
                              sem=sem, gen=gen22)
            a1.save()

            # import smtplib
            # from email.mime.multipart import MIMEMultipart
            # from email.mime.text import MIMEText
            # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            # s.starttls()
            # s.login("rissprjcalicut555@gmail.com", "P09388434043")
            # msg = MIMEMultipart()  # create a message.........."
            # message = "New Passoword"
            # msg['From'] = "rissprjcalicut555@gmail.com"
            # msg['To'] = email
            # msg['Subject'] = "Your Password"
            # body = "Your Password is:- - " + str(rr)
            # msg.attach(MIMEText(body, 'plain'))
            # s.send_message(msg)
            # print("kkkkkk")




            return render(request, "college/home.html")

    return render(request, 'college/student_add.html')


def clg_student_view(request):
    if request.method == "POST":
        b = request.POST["ser"]
        print("jj")
        res = studentmodel.objects.filter(name__startswith=b)
    else:

        res = studentmodel.objects.all()

    return render(request, "college/student_view.html", {'res': res})


def clg_student_edit(request, id):
    res = studentmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"] = id

    return render(request, 'college/student_edit.html', {'res': res})


@csrf_exempt
def clg_student_edit_post(request):
    print("qqq")
    id = request.session["id"]

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
    lob_ob = loginmodel.objects.get(id=cid)
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
        # tst
        from datetime import datetime
        date_format = "%Y-%m-%d"
        start = datetime.strptime(dob, date_format)
        now = datetime.now()
        if now < start:
            print("ys")
            return HttpResponse("Please check Date")
        else:
            print("nn")

            res.name = name22
            res.img = fs.url(name)
            res.place = place
            res.house = house
            res.post = post
            res.city = city
            res.email = email
            res.phone = phone
            res.dob = dob
            res.department = department
            res.sem = sem
            res.gen = gen

            # res.description=dis
            res.save()

            return render(request, "college/home.html")
    return render(request, 'college/student_edit.html', {'res': res})


def clg_student_del(request, id):
    res = studentmodel.objects.get(id=id)
    res.delete()
    return render(request, "college/home.html")


def clg_assign_phycaltrainr(request):
    if request.method == "POST":
        cid = request.POST["cid"]
        mmss = sports_catmodel.objects.get(id=cid)

        sid = request.POST["sid"]
        mmss2 = staffmodel.objects.get(id=sid)

        import datetime
        yy = datetime.datetime.now().strftime("%Y-%m-%d")
        print("ss=", yy)

        a1 = assign_cate_model(SPORTS_CATE=mmss, STAFF=mmss2, date=yy)
        a1.save()

        return render(request, "college/home.html")
    res = sports_catmodel.objects.all()
    ck = request.session["lid"]
    cm = collegemodel.objects.get(LID=ck)
    log_ob = loginmodel.objects.filter(type='phy')
    res2 = []
    for i in log_ob:
        print("entr")
        print(i)
        qq = i.id
        print("qq=", qq)
        log_obnew = loginmodel.objects.get(id=qq)
        print("qs")
        print(log_obnew)
        stf_new = staffmodel.objects.get(LOGIN=log_obnew)
        print(stf_new)
        print("qwe")
        s = {'id': stf_new.id, 'name': stf_new.name}
        res2.append(s)
        print("yyy")

    print("ovr")

    print(res2)

    return render(request, 'college/assign_sports_cate_staff.html', {'res': res, 'res2': res2})


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

        desi = request.POST["desi"]
        status = "pending"
        email = request.POST['email']
        import random
        rr = random.randint(0000, 9999)
        b1 = loginmodel(uname=email, pwd=rr, type="eventorg")
        b1.save()
        ab = loginmodel.objects.latest('id')
        print("ab=", ab.pk)

        mmss = loginmodel.objects.get(id=ab.pk)

        a1 = eventorgizermodel(LOGIN=mmss, name=name22, ph=ph, details=details, image=fs.url(name), desi=desi,
                               status=status, email=email)
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
        type22 = "clg"
        import datetime
        yy = datetime.datetime.now().strftime("%Y-%m-%d")
        print("ss=", yy)
        a1 = notificationmodel(msg=msg, datee=yy, type=type22)
        a1.save()

        return render(request, "college/home.html")
    return render(request, 'college/Notification_add.html')


def clg_adm_notif_view(request):
    res = notificationmodel.objects.all()

    return render(request, "college/View_notification.html", {'res': res})


def clgadm_noti_edit(request, id):
    res = notificationmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"] = id

    return render(request, 'college/edit_notifi.html', {'res': res})


@csrf_exempt
def clg_adm_noti_post(request):
    id = request.session["id"]

    na1 = request.POST["textfield"]

    res = notificationmodel.objects.get(id=id)

    if request.method == "POST":
        res.msg = na1
        # res.description=dis
        res.save()

        return render(request, "college/home.html")
    return render(request, 'college/edit_notifi.html', {'res': res})


def clg_adm_noti_del(request, id):
    res = notificationmodel.objects.get(id=id)
    res.delete()
    return render(request, "college/home.html")


def clg_college_profile(request):
    rr = request.session["lid"]
    kk = loginmodel.objects.get(id=rr)
    res = collegemodel.objects.get(LID=kk)

    return render(request, 'college/View_profile.html', {'i': res})


def phy_assign_clgteam_std(request):
    if request.method == "POST":
        tm = request.POST["cid"]
        std = request.POST["sid"]
        s1 = studentmodel.objects.get(id=std)
        t1 = collegeteammodel.objects.get(id=tm)

        a1 = team_member_model(STUDENT=s1, TEAM=t1)
        a1.save()

        return render(request, "physical/home.html")
    print("h")
    cid = request.session["lid"]
    print("cid=", cid)
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)
    sidd = ms.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=sidd)
    msk = collegeteammodel.objects.filter(COLLEGE=clg_ob)
    print(msk)
    print("uu")

    std = studentmodel.objects.filter(COLLEGE=clg_ob)
    print("ms")

    return render(request, 'physical/encroll_std_clg_team.html', {'res': msk, 'res2': std})


def phy_traing_sch_Cat(request):
    if request.method == "POST":
        t1 = request.POST['time_from']
        t2 = request.POST["time_to"]
        d1 = request.POST["datee"]
        cid = request.POST["cid"]
        ob = collegeteammodel.objects.get(id=cid)

        a1 = schedulemodel(time_from=t1, time_to=t2, datee=d1, COLLEGETEAM=ob)
        a1.save()

        return render(request, "physical/home.html")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    msk = collegeteammodel.objects.filter(STAFF=ms)

    return render(request, 'physical/traing_sc_add.html', {'res': msk})


def phy_traing_sch_view(request):
    res = schedulemodel.objects.all()

    return render(request, "physical/train_sc_view.html", {'res': res})


def phy_traing_sch_edit(request, id):
    res = schedulemodel.objects.get(id=id)
    print(res)
    request.session["id"] = id

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    msk = collegeteammodel.objects.filter(STAFF=ms)

    return render(request, 'physical/traing_sc_update.html', {'i': res, 'res': msk})


@csrf_exempt
def phy_traing_sch_post(request):
    print("hhh")
    id = request.session["id"]

    t1 = request.POST['time_from']
    t2 = request.POST["time_to"]
    d1 = request.POST["datee"]
    cid = request.POST["cid"]
    ob = collegeteammodel.objects.get(id=cid)

    res = schedulemodel.objects.get(id=id)

    if request.method == "POST":
        res.time_from = t1
        res.time_to = t2
        res.datee = d1
        res.COLLEGETEAM = ob
        res.save()

        return render(request, "physical/home.html")
    return render(request, 'physical/traing_sc_update.html', {'res': res})


def phy_traing_sch_del(request, id):
    res = schedulemodel.objects.get(id=id)
    res.delete()
    return render(request, "physical/home.html")


####

def phy_sports_profile(request):
    if request.method == "POST":
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime = datetime.date.today()

        n1 = request.POST['name']
        p1 = request.POST["position"]
        d1 = showtime
        cid = request.POST["cid"]
        des = request.POST["des"]

        ob = studentmodel.objects.get(id=cid)

        a1 = sports_profilemodel(name=n1, position=p1, desc=des, date=d1, STUDENT=ob)
        a1.save()

        return render(request, "physical/home.html")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)
    clg_id = ms.COLLEGE.id

    clg_ob = collegemodel.objects.get(id=clg_id)
    print("ss")
    print(clg_ob)
    msk = studentmodel.objects.filter(COLLEGE=clg_ob)
    print(msk)

    return render(request, 'physical/sport_profile_add.html', {'res': msk})


def phy_sports_profile_view(request):
    res = sports_profilemodel.objects.all()

    return render(request, "physical/view_sprt_prfl_update.html", {'res': res})


def phy_sports_profile_edit(request, id):
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
        showtime = datetime.date.today()

        date22 = showtime
        # date22 = request.POST['date']
        ctype = request.POST['contnt_type']
        upload_file = request.FILES['path']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/fil/" + upload_file.name
        desci = request.POST['desci']

        cid = request.session["lid"]
        print("cid=", cid)
        log_ob = loginmodel.objects.get(id=cid)
        mmss22 = staffmodel.objects.get(LOGIN=log_ob)
        print(mmss22)

        a1 = motivationmodel(date=date22, contnt_type=ctype, path=fs.url(name), desci=desci, STAFF=mmss22)
        a1.save()

        return render(request, "physical/home.html")

    return render(request, 'physical/motiv_add.html')


def clg_evnt_add(request):
    if request.method == "POST":
        d1 = request.POST['date']
        e1 = request.POST['ename']
        des = request.POST['descri']
        etype = request.POST['etype']
        cid = request.session["lid"]
        log_ob = loginmodel.objects.get(id=cid)
        mmss22 = collegemodel.objects.get(LID=log_ob)

        a1 = eventmodel(date=d1, descri=des, etype=etype, COLLEGE=mmss22, ename=e1)
        a1.save()

        return render(request, "college/home.html")
    return render(request, 'college/event_add.html')


def clg_evnt_view(request):
    if request.method == "POST":
        print("qq")
        d1 = request.POST["d1"]
        d2 = request.POST["d2"]
        print("qq")
        cc = eventmodel.objects.filter(date__gte=d1, date__lte=d2)
        print(cc)
        return render(request, "college/event_view.html", {'res': cc})

    print("hlw")
    cid = request.session["lid"]
    print(cid)
    log_ob = loginmodel.objects.get(id=cid)
    mmss22 = collegemodel.objects.get(LID=log_ob)
    print(mmss22)

    res = eventmodel.objects.filter(COLLEGE=mmss22)
    print(res)

    return render(request, "college/event_view.html", {'res': res})


def clgadm_evnt_edit(request, id):
    res = eventmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"] = id

    return render(request, 'college/event_edit.html', {'i': res})


@csrf_exempt
def clg_evnt_post(request):
    id = request.session["id"]
    d1 = request.POST['date']
    e1 = request.POST['ename']
    des = request.POST['descri']
    etype = request.POST['etype']
    cid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=cid)
    mmss22 = collegemodel.objects.get(LID=log_ob)

    res = eventmodel.objects.get(id=id)

    if request.method == "POST":
        res.date = d1
        res.descri = des
        res.etype = etype
        res.COLLEGE = mmss22
        res.ename = e1
        # res.description=dis
        res.save()

        return render(request, "college/home.html")
    return render(request, 'college/event_edit.html', {'res': res})


def clg_evnt_del(request, id):
    res = eventmodel.objects.get(id=id)
    res.delete()
    return render(request, "college/home.html")


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
    lid = request.session["lid"]
    log_ob = loginmodel.objects.get(pk=lid)

    res = staffmodel.objects.get(LOGIN=log_ob)

    return render(request, "nutition/view profile.html", {'res': res})


def nut_staff_edit(request):
    lid = request.session["lid"]
    log_ob = loginmodel.objects.get(pk=lid)
    res = staffmodel.objects.get(LOGIN=log_ob)

    print(res)
    print("qq")
    # request.session["id"]=id

    return render(request, 'nutition/edit_nutrn.html', {'res': res})


@csrf_exempt
def nut_staff_edit_post(request):
    print("qq")
    lid = request.session["lid"]
    log_ob = loginmodel.objects.get(pk=lid)
    res55 = staffmodel.objects.get(LOGIN=log_ob)
    print(res55)

    id = res55

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
        res.name = name22
        res.image = fs.url(name)
        res.dob = dob
        res.place = place
        res.gen = gen
        res.city = city
        res.state = state
        res.pin = pin
        res.type = 'nut'
        res.phone = phone

        # res.description=dis
        res.save()

        return render(request, "nutition/home.html")
    return render(request, 'nutition/edit_nutrn.html', {'res': res})


# def nut_staff_del(request, id):
#     res = staffmodel.objects.get(id=id)
#     res.delete()
#     return  render(request,"nutition/home.html")


def nut_add(request):
    if request.method == "POST":
        n1 = request.POST['name']
        p1 = request.POST["descri"]
        lid = request.session["lid"]
        li_ob = loginmodel.objects.get(id=lid)
        st_ob = staffmodel.objects.get(LOGIN=li_ob)
        print("jjj")

        ob = st_ob.COLLEGE.id
        clg_ob = collegemodel.objects.get(id=ob)
        print("hlw")
        print(clg_ob)

        a1 = nutritionmodel(name=n1, descri=p1, CLG=clg_ob)
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


def nut_edit(request, id):
    res = nutritionmodel.objects.get(id=id)
    request.session["id"] = id

    # cid = request.POST["lid"]
    # mmss = loginmodel.objects.get(id=cid)
    # ms = staffmodel.objects.get(LOGIN=mmss)
    # clg_id = ms.COLLEGE.id
    # clg_ob = collegeteammodel.objects.get(id=clg_id)
    #
    return render(request, 'nutition/nut_edit.html', {'i': res})


@csrf_exempt
def nut_post(request):
    id22 = request.session["id"]

    n1 = request.POST['name']
    p1 = request.POST["descri"]
    lid = request.session["lid"]
    li_ob = loginmodel.objects.get(id=lid)
    st_ob = staffmodel.objects.get(LOGIN=li_ob)

    ob = st_ob.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=ob)

    res = nutritionmodel.objects.get(id=id22)

    if request.method == "POST":
        res.name = n1
        res.descri = p1
        res.CLG = clg_ob
        res.save()

        return render(request, "nutition/home.html")
    return render(request, 'nutition/nut_edit.html', {'res': res})


def nut_del(request, id):
    res = nutritionmodel.objects.get(id=id)
    res.delete()
    return render(request, "nutition/home.html")


def nut_allo_add(request):
    if request.method == "POST":
        q1 = request.POST['quantity']
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime = datetime.date.today()
        d1 = showtime
        nid = request.POST["nid"]
        studid = request.POST["cid"]
        nu_ob = nutritionmodel.objects.get(id=nid)

        ob = studentmodel.objects.get(id=studid)

        a1 = nutritionallocationmodel(quantity=q1, datee=d1, NUTRITION=nu_ob, STUDENT=ob)
        a1.save()

        return render(request, "nutition/home.html")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    ms = staffmodel.objects.get(LOGIN=mmss)
    clg_id = ms.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=clg_id)
    print(clg_ob)
    msk = studentmodel.objects.filter(COLLEGE=clg_ob)
    print("ss")
    print(msk)
    msk2 = nutritionmodel.objects.filter(CLG=clg_ob)

    return render(request, 'nutition/nutrion_allocn_add.html', {'res': msk, 'res2': msk2})


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
    return render(request, "nutition/home.html")


def chatload(request):
    return render(request, 'nutition/fur_chat.html')


def drviewmsg(request, receiverid):
    doclidlid = request.session["lid"]
    print("!!!!!!!!!!", doclidlid, receiverid)
    log_ob = loginmodel.objects.get(id=doclidlid)
    doc = staffmodel.objects.get(LOGIN=log_ob)
    print(doc)
    # stud_ob=studentmodel.objects.get(LID=rec)
    lll = loginmodel.objects.get(id=receiverid)
    print("jjj")
    print(lll)
    xx = studentmodel.objects.get(id=receiverid)
    print(xx)
    print("xx ovr")
    obj = chat_staff.objects.filter(FID=doc, UID=xx)
    print(obj)
    user_data = studentmodel.objects.get(id=receiverid)
    print(user_data)
    print("********************", obj)

    res = []
    for i in obj:
        s = {'id': i.pk, 'date': i.date, 'msg': i.message, 'type': i.type}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res, 'name': user_data.name, 'image': user_data.img})


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
    da = studentmodel.objects.filter(COLLEGE=clg_ob)
    print(da)
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.name, 'email': i.email, 'image': i.img}
        res.append(s)
    print(res)

    return JsonResponse({'status': 'ok', 'data': res})


def doctor_insert_chat(request, receiverid, msg):
    print("hai riss")

    dlid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=dlid)
    dobj = staffmodel.objects.get(LOGIN=log_ob)
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime = datetime.datetime.now()
    print("qqq")

    obj = chat_staff()
    obj.UID = studentmodel.objects.get(pk=receiverid)
    obj.FID = dobj
    obj.message = msg
    obj.type = 'fuser'
    obj.date = showtime
    obj.save()
    print("yyy")

    return JsonResponse({'status': 'ok'})


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
        clg_id = stf_ob.COLLEGE.id
        clg_ob = collegemodel.objects.get(id=clg_id)
        print(clg_ob)
        print("ww")

        a1 = collegeteammodel(namee=t1, datee=t2, STAFF=stf_ob, COLLEGE=clg_ob)
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


def phy_team_edit(request, id):
    print("QQQ")
    res = collegeteammodel.objects.get(id=id)
    request.session["id"] = id

    # cid = request.session["lid"]
    # mmss = loginmodel.objects.get(id=cid)
    # ms = staffmodel.objects.get(LOGIN=mmss)
    # print(ms)
    # msk = collegeteammodel.objects.get(STAFF=ms)
    # print(msk)


    return render(request, 'physical/Team_edit.html', {'i': res})


@csrf_exempt
def phy_team_post(request):
    id = request.session["id"]

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
    t2 = yy
    print("hls")

    if request.method == "POST":
        res.namee = t1
        res.datee = t2
        res.COLLEGE = clg_ob
        res.STAFF = stf_ob
        res.save()

        return render(request, "physical/home.html")
    return render(request, 'physical/Team_edit.html', {'res': res})


def phy_team_del(request, id):
    res = collegeteammodel.objects.get(id=id)
    res.delete()
    return render(request, "physical/home.html")


##

def nut_msg_add(request):
    if request.method == "POST":
        print("kk")
        t1 = request.POST['msg']
        t2 = request.POST['mtype']
        nn = request.POST['nn']
        import datetime
        yy = datetime.datetime.now().strftime("%Y-%m-%d")
        t3 = yy
        nut_ob = nutritionmodel.objects.get(id=nn)

        a1 = msg_nutitionnist_model(msg=t1, datee=t3, mtype=t2, NUTRITION=nut_ob)
        a1.save()

        return render(request, "nutition/home.html")

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

    return render(request, 'nutition/msg_add.html', {'res': rrr})


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


def nut_msg_edit(request, id):
    res = msg_nutitionnist_model.objects.get(id=id)
    request.session["id"] = id

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

    return render(request, 'nutition/msg_edit.html', {'i': res, 'rrr': rrr})


@csrf_exempt
def nut_msg_post(request):
    id = request.session["id"]

    cid = request.session["lid"]

    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    stf_ob = staffmodel.objects.get(LOGIN=mmss)
    print(stf_ob)
    t1 = request.POST['msg']
    t2 = request.POST['mtype']
    nut = request.POST['nn']
    nut_ob = nutritionmodel.objects.get(id=nut)

    import datetime
    yy = datetime.datetime.now().strftime("%Y-%m-%d")
    t3 = yy

    res = msg_nutitionnist_model.objects.get(id=id)
    print("hj")

    if request.method == "POST":
        res.msg = t1
        res.datee = t3
        res.mtype = t2
        res.NUTRITION = nut_ob
        res.save()

        return render(request, "nutition/home.html")
    return render(request, 'nutition/msg_edit.html', {'res': res})


def nut_msg_del(request, id):
    res = msg_nutitionnist_model.objects.get(id=id)
    res.delete()
    return render(request, "nutition/home.html")


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
    return render(request, "physical/home.html")


##################################
def pub_home(request):
    return render(request, "public/home.html")


def pub_notif_view(request):
    res = notificationmodel.objects.all()

    return render(request, "public/notif.html", {'res': res})


def pub_college_view(request):
    if request.method == "POST":
        b = request.POST["ser"]
        print("jj")
        res = collegemodel.objects.filter(name__startswith=b)
    else:

        res = collegemodel.objects.all()

    return render(request, "public/viw_clg.html", {'res': res})


def phy_glry_add(request):
    if request.method == "POST":
        print("jj22")
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime = datetime.datetime.now()
        print("QQQ")

        date22 = showtime
        # date22 = request.POST['date']
        desi = request.POST['desi']
        print("qqq22")
        upload_file = request.FILES['img']
        print("qqq")
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/gal/" + upload_file.name

        cid = request.session["lid"]
        print("cid=", cid)
        log_ob = loginmodel.objects.get(id=cid)
        mmss22 = staffmodel.objects.get(LOGIN=log_ob)
        print(mmss22)
        eid = request.POST["evnt"]
        evnt_ob = eventmodel.objects.get(id=eid)

        a1 = gallerymodel(STAFF=mmss22, EVENT=evnt_ob, img=fs.url(name), datee=showtime, desi=desi)
        a1.save()

        return render(request, "physical/home.html")

    lid = request.session["lid"]
    log_obj = loginmodel.objects.get(id=lid)
    stff_obj = staffmodel.objects.get(LOGIN=log_obj)
    cid = stff_obj.COLLEGE_id
    evnt_obj = eventmodel.objects.filter(COLLEGE_id=cid)
    return render(request, 'physical/gallry_add.html', {'res': evnt_obj})


def phy_gal_view(request):
    print("hhh")

    cid = request.session["lid"]
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)

    res = gallerymodel.objects.filter(STAFF=ms)
    print(res)
    # res33=nutritionallocationmodel.objects.all()

    return render(request, "physical/gallay_view.html", {'res': res})


def phy_gal_del(request, id):
    res = gallerymodel.objects.get(id=id)
    res.delete()
    return render(request, "physical/home.html")


def pub_gal_view(request):
    print("hhh")

    res = gallerymodel.objects.all()
    print(res)
    # res33=nutritionallocationmodel.objects.all()

    return render(request, "public/gallery_view.html", {'res': res})


def nut_alloc_rept_view(request):
    print("hhh")
    print("hhh")
    if request.method == 'POST':
        d1 = request.POST["d1"]
        d2 = request.POST["d2"]
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
            # rk22 = nutritionallocationmodel.objects.filter(NUTRITION=nut_obnew,datee__range=[d1, d2])
            # rk22 =  nutritionallocationmodel.objects.filter(datee__gte='2021-03-01', datee__lte='2021-05-13')
            rk22 = nutritionallocationmodel.objects.filter(datee__gte=d1, datee__lte=d2, NUTRITION=nut_obnew, )

            print(rk22)
            for rk in rk22:
                print("jk")

                s = {'pk': rk.id, 'quantity': rk.quantity, 'datee': rk.datee, 'nname': rk.NUTRITION.name,
                     'sname': rk.STUDENT.name, 'place': rk.STUDENT.place, 'image': rk.STUDENT.img,
                     'department': rk.STUDENT.department, 'gen': rk.STUDENT.gen}
                print(s)
                res2.append(s)

            print("jjjj")

            # print(log_obnew)
            # stf_new = staffmodel.objects.get(LOGIN=log_obnew)
            # print(stf_new)
            # print("qwe")

            print("yyy")
        print("loop over")
        print(res2)
        print("ovr")
        # return HttpResponse("jjj")







        # res = nutritionallocationmodel.objects.filter(NUTRITION=kk)
        # print(res)
        #
        #
        return render(request, "nutition/nut_alloc_report.html", {'res': res2})

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
                 'sname': rk.STUDENT.name, 'place': rk.STUDENT.place, 'image': rk.STUDENT.img,
                 'department': rk.STUDENT.department, 'gen': rk.STUDENT.gen}
            # res2.append(s)
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
    return render(request, "nutition/nut_alloc_report.html", {'res': res2})


# chat phy-student
def chatload_phy(request):
    return render(request, 'physical/fur_chat.html')


def drviewmsg_phy(request, receiverid):
    doclidlid = request.session["lid"]
    print("!!!!!!!!!!", doclidlid, receiverid)
    log_ob = loginmodel.objects.get(id=doclidlid)
    doc = staffmodel.objects.get(LOGIN=log_ob)
    print(doc)
    # stud_ob=studentmodel.objects.get(LID=rec)
    lll = loginmodel.objects.get(id=receiverid)
    print("jjj")
    print(lll)
    xx = studentmodel.objects.get(id=receiverid)
    print(xx)
    print("xx ovr")
    obj = chat_staff.objects.filter(FID=doc, UID=xx)
    print(obj)
    user_data = studentmodel.objects.get(id=receiverid)
    print(user_data)
    print("********************", obj)

    res = []
    for i in obj:
        s = {'id': i.pk, 'date': i.date, 'msg': i.message, 'type': i.type}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res, 'name': user_data.name, 'image': user_data.img})


def chatview_phy(request):
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
    da = studentmodel.objects.filter(COLLEGE=clg_ob)
    print(da)
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.name, 'email': i.email, 'image': i.img}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})


def doctor_insert_chat_phy(request, receiverid, msg):
    print("hai riss")

    dlid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=dlid)
    dobj = staffmodel.objects.get(LOGIN=log_ob)
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime = datetime.datetime.now()
    print("qqq")

    obj = chat_staff()
    obj.UID = studentmodel.objects.get(pk=receiverid)
    obj.FID = dobj
    obj.message = msg
    obj.type = 'fuser'
    obj.date = showtime
    obj.save()
    print("yyy")
    return JsonResponse({'status': 'ok'})


# chat phy-user
def chatload_phy_usr(request):
    return render(request, 'physical/chat_carrir.html')


def drviewmsg_phy_usr(request, receiverid):
    doclidlid = request.session["lid"]
    print("!!!!!!!!!!", doclidlid, receiverid)
    log_ob = loginmodel.objects.get(id=doclidlid)
    doc = staffmodel.objects.get(LOGIN=log_ob)
    print(doc)
    # stud_ob=studentmodel.objects.get(LID=rec)
    xx = usermodel.objects.get(id=receiverid)
    print(xx)
    obj = chat.objects.filter(FID=doc, UID=xx)
    print(obj)
    user_data = usermodel.objects.get(id=receiverid)
    print(user_data)
    print("********************", obj)

    res = []
    for i in obj:
        s = {'id': i.pk, 'date': i.date, 'msg': i.message, 'type': i.type}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res, 'name': user_data.name, 'image': user_data.img})


def chatview_phy_usr(request):
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
    da = usermodel.objects.filter(COLLEGE=clg_ob)
    print(da)
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.cname, 'email': i.email, 'image': i.image}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})


def doctor_insert_chat_phy_usr(request, receiverid, msg):
    print("hai riss")

    dlid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=dlid)
    dobj = staffmodel.objects.get(LOGIN=log_ob)
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime = datetime.datetime.now()
    print("qqq")

    obj = chat()
    obj.UID = usermodel.objects.get(pk=receiverid)
    obj.FID = dobj
    obj.message = msg
    obj.type = 'fuser'
    obj.date = showtime
    obj.save()
    print("yyy")
    return JsonResponse({'status': 'ok'})


def carrior_user_add(request):
    if request.method == "POST":
        name22 = request.POST['name']
        cname22 = request.POST['cname']

        upload_file = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/stf/" + upload_file.name
        ph = request.POST['ph']
        details = request.POST['details']
        desi = request.POST["desi"]
        status = "pending"
        email = request.POST['email']
        import random
        rr = random.randint(0000, 9999)
        b1 = loginmodel(uname=email, pwd=rr, type="carrier")
        b1.save()
        ab = loginmodel.objects.latest('id')
        print("ab=", ab.pk)
        mmss = loginmodel.objects.get(id=ab.pk)
        a1 = usermodel(LOGIN=mmss, name=name22, cname=cname22, ph=ph, email=email, details=details, image=fs.url(name),
                       desi=desi, utype='carrier', status='pending')
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

    return render(request, 'carrier/cari_signup.html')


def carrier_portfolio_view(request):
    res = portfoliomodel.objects.all()

    return render(request, "carrier/portfolio_view.html", {'res': res})


def carrier_home(request):
    return render(request, "carrier/home.html")


# chat with carr-phy

def chatload_usr_phy(request):
    return render(request, 'carrier/chat_phy.html')


def drviewmsg_usr_phy(request, receiverid):
    doclidlid = request.session["lid"]
    print("!!!!!!!!!!", doclidlid, receiverid)
    log_ob = loginmodel.objects.get(id=doclidlid)
    doc = usermodel.objects.get(LOGIN=log_ob)
    print(doc)
    # stud_ob=studentmodel.objects.get(LID=rec)
    xx = staffmodel.objects.get(id=receiverid)
    print(xx)
    obj = chat.objects.filter(FID=doc, UID=xx)
    print(obj)
    user_data = staffmodel.objects.get(id=receiverid)
    print(user_data)
    print("********************", obj)

    res = []
    for i in obj:
        s = {'id': i.pk, 'date': i.date, 'msg': i.message, 'type': i.type}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res, 'name': user_data.name, 'image': user_data.img})


def chatview_usr_phy(request):
    print("hai")
    cid = request.session["lid"]
    print(cid)
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = usermodel.objects.get(LOGIN=mmss)
    print(ms)
    da = staffmodel.objects.all()
    print(da)
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.name, 'email': i.email, 'image': i.image}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})


def doctor_insert_chat_usr_phy(request, receiverid, msg):
    print("hai riss")

    dlid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=dlid)
    dobj = usermodel.objects.get(LOGIN=log_ob)
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime = datetime.datetime.now()
    print("qqq")

    obj = chat()
    obj.UID = staffmodel.objects.get(pk=receiverid)
    obj.FID = dobj
    obj.message = msg
    obj.type = 'nuser'
    obj.date = showtime
    obj.save()
    print("yyy")
    return JsonResponse({'status': 'ok'})


def event_home(request):
    return render(request, "event_orgizr/home.html")


def evnt_org_evnt_add(request):
    if request.method == "POST":
        d1 = request.POST['date']
        e1 = request.POST['ename']
        des = request.POST['descri']
        etype = request.POST['etype']
        cid = request.session["lid"]
        log_ob = loginmodel.objects.get(id=cid)
        mmss22 = collegemodel.objects.get(LID=log_ob)

        a1 = eventmodel(date=d1, descri=des, etype=etype, COLLEGE=mmss22, ename=e1)
        a1.save()

        return render(request, "college/home.html")
    return render(request, 'college/event_add.html')


def evnt_org_evnt_view(request):
    print("hlw")
    cid = request.session["lid"]
    print(cid)
    log_ob = loginmodel.objects.get(id=cid)
    mmss22 = eventorgizermodel.objects.get(LID=log_ob)
    print(mmss22)

    res = event2model.objects.filter(LOGIN=mmss22)
    print(res)

    return render(request, "event_orgizr/event_view.html", {'res': res})


def evnt_orgadm_evnt_edit(request, id):
    res = eventmodel.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"] = id

    return render(request, 'event_orgizr/event_edit.html', {'i': res})


@csrf_exempt
def evnt_org_evnt_post(request):
    id = request.session["id"]
    d1 = request.POST['date']
    e1 = request.POST['ename']
    des = request.POST['descri']
    etype = request.POST['etype']
    cid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=cid)
    mmss22 = eventorgizermodel.objects.get(LOGIN=log_ob)

    res = event2model.objects.get(id=id)

    if request.method == "POST":
        res.date = d1
        res.descri = des
        res.etype = etype
        res.COLLEGE = mmss22
        res.ename = e1
        # res.description=dis
        res.save()

        return render(request, "event_orgizr/home.html")
    return render(request, 'event_orgizr/event_edit.html', {'res': res})


def evnt_org_evnt_del(request, id):
    res = event2model.objects.get(id=id)
    res.delete()
    return render(request, "event_orgizr/home.html")


#####3 scrime
def clg_paricipants(request):
    print("hlw")
    cid = request.session["lid"]
    print(cid)
    log_ob = loginmodel.objects.get(id=cid)
    clg_og = collegemodel.objects.get(LID=log_ob)
    mmss22 = studentmodel.objects.filter(COLLEGE=clg_og)
    res2 = []
    print(mmss22)
    for i in mmss22:
        print("qqq")

        r4 = participantmodel.objects.filter(STUDENT=i, status='pending')
        for j in r4:
            ss = {'id': i.pk, 'sname': j.STUDENT.name, 'event': j.EVENT.ename, 'date': j.EVENT.date,
                  'descri': j.EVENT.descri, 'etype': j.EVENT.etype}
            res2.append(ss)

    return render(request, "college/particpnt_view.html", {'res': res2})


def clg_paricipants_acpt(request):
    print("hlw")
    cid = request.session["lid"]
    print(cid)
    log_ob = loginmodel.objects.get(id=cid)
    clg_og = collegemodel.objects.get(LID=log_ob)
    mmss22 = studentmodel.objects.filter(COLLEGE=clg_og)
    res2 = []
    print(mmss22)
    for i in mmss22:
        print("qqq")

        r4 = participantmodel.objects.filter(STUDENT=i, status='accept')
        for j in r4:
            ss = {'id': i.pk, 'sname': j.STUDENT.name, 'event': j.EVENT.ename, 'date': j.EVENT.date,
                  'descri': j.EVENT.descri, 'etype': j.EVENT.etype}
            res2.append(ss)

    return render(request, "college/participant_accpt.html", {'res': res2})


def clg_paricipants_accept(request, id):
    print("hlw")
    res = participantmodel.objects.get(id=id)
    res.status = 'accept'
    res.save()
    return render(request, "college/home.html")


def clg_paricipants_reject(request, id):
    res = participantmodel.objects.get(id=id)
    res.status = 'reject'
    res.save()
    return render(request, "college/home.html")


# chat clg-student
def chatload_clg(request):
    return render(request, 'college/fur_chat.html')


def drviewmsg_clg(request, receiverid):
    doclidlid = request.session["lid"]
    print("!!!!!!!!!!", doclidlid, receiverid)
    log_ob = loginmodel.objects.get(id=doclidlid)
    doc = collegemodel.objects.get(LID=log_ob)
    print(doc)
    xx = loginmodel.objects.get(id=receiverid)
    print("www")
    print(xx)
    stud_ob = studentmodel.objects.get(LID=xx)

    obj = chat.objects.filter(FID=doc, UID=stud_ob)
    print(obj)
    print("erer")
    user_data = studentmodel.objects.get(LID=xx)
    print(user_data)

    print("********************", obj)

    res = []
    for i in obj:
        s = {'id': i.pk, 'date': i.date, 'msg': i.message, 'type': i.type}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res, 'name': user_data.name, 'image': user_data.img})


def chatview_clg(request):
    print("hai")
    cid = request.session["lid"]
    print(cid)
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = collegemodel.objects.get(LID=mmss)
    print(ms)

    da = studentmodel.objects.filter(COLLEGE=ms)
    print(da)
    res = []
    for i in da:
        s = {'id': i.LID_id, 'name': i.name, 'email': i.email, 'image': i.img}
        print(s)
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})


def doctor_insert_chat_clg(request, receiverid, msg):
    print("hai riss")

    dlid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=dlid)
    dobj = collegemodel.objects.get(LID=log_ob)
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime = datetime.datetime.now()
    print("qqq")
    print(receiverid)
    st_lgn = loginmodel.objects.get(id=receiverid)

    print("ss")

    obj = chat()
    obj.UID = studentmodel.objects.get(LID=st_lgn)
    obj.FID = dobj
    obj.message = msg
    obj.type = 'fuser'
    obj.date = showtime
    obj.save()
    print("yyy")
    return JsonResponse({'status': 'ok'})


def user_login(request):
    print("hlw22")
    if request.method == "POST":
        print("qqq")
        username = request.POST['username']
        password = request.POST['password']
        print("ss")
        try:
            log_obj = loginmodel.objects.filter(uname=username, pwd=password)
            print(log_obj)
            if log_obj.exists():
                print("qqq22")
                logg = log_obj[0]

                qq = logg.id
                print(qq)
                sy = loginmodel.objects.get(uname=username, pwd=password)
                if sy.type == "student":
                    print("entr")
                    std_obj = studentmodel.objects.get(LID=sy)
                    print(std_obj)

                    data = {"status": "ok", "lid": qq, 'college_id': std_obj.COLLEGE.id}
                    return JsonResponse(data)

                else:
                    data = {"status": "no"}
                    return JsonResponse(data)

            else:
                data = {"status": "no"}
                return JsonResponse(data)

        except Exception as e:
            return e


def user_view_profile(request):
    print("entr pr")
    lid = request.POST['lid']
    log_obj = loginmodel.objects.get(id=lid)
    print("qqq")
    user_obj = studentmodel.objects.get(LID=log_obj)
    print(user_obj)

    data = {"status": "ok", 'name': user_obj.name, 'place': user_obj.place, 'img': user_obj.img,
            'house': user_obj.house, 'post': user_obj.post, 'phone': user_obj.phone, 'gen': user_obj.gen}
    return JsonResponse(data)


def user_view_portifolio(request):
    print("hlw")
    lid = request.POST['lid']
    print(lid)
    log_obj = loginmodel.objects.get(id=lid)
    print(log_obj)
    user_obj = studentmodel.objects.get(LID=log_obj)
    print(user_obj)
    port_obj22 = portfoliomodel.objects.filter(STUDENT=user_obj)
    print(port_obj22)
    res2 = []
    for port_obj in port_obj22:
        print("qq")

        ss = {"status": "ok", 'achievement': port_obj.achievement, 'date': port_obj.date, 'position': port_obj.position}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def user_view_teammembrs(request):
    lid = request.POST['lid']
    log_obj = loginmodel.objects.get(id=lid)
    user_obj = studentmodel.objects.get(LID=log_obj)
    team_obj22 = team_member_model.objects.filter(STUDENT=user_obj)
    res2 = []
    for team_obj in team_obj22:
        print("qqq")

        ss = {"status": "ok", 'name': team_obj.TEAM.namee, 'date': team_obj.TEAM.datee}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def usr_view_motivation(request):
    res2 = []

    team_obj22 = motivationmodel.objects.all()
    for team_obj in team_obj22:
        print("qqq")

        ss = {"status": "ok", 'path': team_obj.path, 'date': team_obj.date, 'contnt_type': team_obj.contnt_type,
              'desci': team_obj.desci}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def usr_view_notif(request):
    res2 = []
    team_obj22 = notificationmodel.objects.all()
    for team_obj in team_obj22:
        print("qq")

        ss = {"status": "ok", 'msg': team_obj.msg, 'datee': team_obj.datee, 'type': team_obj.type}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def usr_view_msg_from_nutrilst(request):
    print("qqq22")

    cid = request.POST['college_id']
    print(cid)
    log_obj = collegemodel.objects.get(id=cid)
    print(log_obj)
    nut_obj = nutritionmodel.objects.filter(CLG=log_obj)
    print("yyy")
    print(nut_obj)
    res2 = []
    if nut_obj.exists():
        print("yes")

        for i in nut_obj:
            print("enr")
            print(i.pk)
            try:

                print("tt")
                msg_nut_obj = msg_nutitionnist_model.objects.filter(NUTRITION_id=i.pk)
                print(msg_nut_obj)
                for j in msg_nut_obj:
                    print("qq")

                    ss = {'id': j.id, 'datee': j.datee, 'msg': j.msg, 'mtype': j.mtype}
                    print(ss)
                    res2.append(ss)
                print(res2)
                print("************")
                data = {"status": "ok", "res2": res2}
                return JsonResponse(data)
            except:
                print("no")
                data = {"status": "no", "res2": res2}
                return JsonResponse(data)


    else:
        print("no")
        data = {"status": "no", "res2": res2}
        return JsonResponse(data)


def usr_view_cmt_reply(request):
    lid = request.POST['lid']
    log_obj = loginmodel.objects.get(id=lid)
    user_obj = studentmodel.objects.get(LID=log_obj)

    team_obj22 = complaintmodel.objects.filter(STUDENT=user_obj)
    res2 = []
    for team_obj in team_obj22:
        print("qq")

        ss = {"status": "ok", 'cmt': team_obj.cmt, 'datee': team_obj.datee, 'reply': team_obj.reply}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def usr_add_cmt(request):
    if request.method == "POST":
        print("hlw")
        cmt = request.POST['cmt']

        lid = request.POST['lid']
        log_obj = loginmodel.objects.get(id=lid)
        user_obj = studentmodel.objects.get(LID=log_obj)

        import datetime
        ddd = datetime.date.today()

        log_obj = complaintmodel()
        log_obj.cmt = cmt
        log_obj.datee = ddd
        log_obj.reply = 'pending'
        log_obj.STUDENT = user_obj

        log_obj.save()

        data = {"status": "ok"}
        return JsonResponse(data)


def usr_view_staff_chat1(request):
    print("mm")
    cid = request.POST['college_id']
    log_obj = collegemodel.objects.get(id=cid)
    print(log_obj)

    stf_obj22 = staffmodel.objects.filter(COLLEGE=log_obj)
    print(stf_obj22)
    res2 = []
    for stf_obj in stf_obj22:
        print("ss")

        ss = {"status": "ok", 'name': stf_obj.name, 'image': stf_obj.image, 'type': stf_obj.type,
              'phone': stf_obj.phone, 'id': stf_obj.pk}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def usr_view_college_chat1(request):
    print("helw")
    cid = request.POST['college_id']
    print(cid)
    log_obj = collegemodel.objects.get(id=cid)
    print(log_obj)

    data = {"status": "ok", 'name': log_obj.name, 'img': log_obj.img, 'place': log_obj.place, 'phone': log_obj.phone,
            'id': log_obj.pk}
    print(data)
    return JsonResponse(data)


def api_Sendmessage(request):
    print("ppppp")
    if request.method == "POST":
        print("ss")
        ulid = request.POST["from_id"]
        did = request.POST["to_id"]
        msgs = request.POST["message"]
        print("fid=", ulid)
        print("toid=", did)
        print("yyy")
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime = datetime.datetime.now()
        msg = chat_staff()

        msg.UID = studentmodel.objects.get(LID=loginmodel.objects.get(pk=ulid))
        msg.FID = staffmodel.objects.get(pk=did)

        msg.message = msgs
        msg.date = showtime
        msg.type = "user"
        msg.save()

        return JsonResponse({'status': 'ok'})


def api_Sendmessage_clg(request):
    print("ppppp")
    if request.method == "POST":
        print("ss")
        ulid = request.POST["from_id"]
        did = request.POST["to_id"]
        msgs = request.POST["message"]
        print("fid=", ulid)
        print("toid=", did)
        print("yyy")
        import datetime
        datetime.date.today()  # Returns 2018-01-15
        showtime = datetime.datetime.now()
        msg = chat()

        msg.UID = studentmodel.objects.get(LID=loginmodel.objects.get(pk=ulid))
        msg.FID = collegemodel.objects.get(pk=did)

        msg.message = msgs
        msg.date = showtime
        msg.type = "user"
        msg.save()

        return JsonResponse({'status': 'ok'})


def api_chatview(request):
    if request.method == "POST":
        print("hlw22")
        ulid = request.POST["ulid"]
        did = request.POST["did"]
        lastmid = request.POST["lastid"]

        print("lst=", lastmid)
        print("ulid=", ulid)
        print("did=", did)

        usr = studentmodel.objects.get(LID=loginmodel.objects.get(pk=ulid))

        print(usr)

        print("qqq")

        dctr = staffmodel.objects.get(pk=did)
        print(dctr)

        cha = chat_staff.objects.filter(UID=usr, FID=dctr, pk__gt=lastmid)
        print(cha)
        print("$$$$$$$$$$$$$$$$$$$$$$")
        print(cha)

        if cha.exists():
            print("entr")
            a = []
            for i in cha:
                a.append({'id': i.pk, 'msg': i.message, 'date': i.date, 'type': i.type})
            print("wwwwwwwwwwwwwwwww")
            print(a)
            print("^^^^^^^^^^^^^^^^^")
            return JsonResponse({'status': 'ok', 'data': a})
        else:
            return JsonResponse({'status': 'no'})


def api_chatview_clg(request):
    if request.method == "POST":
        print("hlw22")
        ulid = request.POST["ulid"]
        did = request.POST["did"]
        lastmid = request.POST["lastid"]

        print("lst=", lastmid)
        print("ulid=", ulid)
        print("did=", did)

        usr = studentmodel.objects.get(LID=loginmodel.objects.get(pk=ulid))

        print(usr)

        print("qqq")

        dctr = collegemodel.objects.get(pk=did)
        print(dctr)

        cha = chat.objects.filter(UID=usr, FID=dctr, pk__gt=lastmid)
        print(cha)
        print("$$$$$$$$$$$$$$$$$$$$$$")
        print(cha)

        if cha.exists():
            print("entr")
            a = []
            for i in cha:
                a.append({'id': i.pk, 'msg': i.message, 'date': i.date, 'type': i.type})
            print("wwwwwwwwwwwwwwwww")
            print(a)
            print("^^^^^^^^^^^^^^^^^")
            return JsonResponse({'status': 'ok', 'data': a})
        else:
            return JsonResponse({'status': 'no'})


def usr_view_college_evnt(request):
    cid = request.POST['college_id']
    log_obj = collegemodel.objects.get(id=cid)

    stf_obj22 = eventmodel.objects.filter(COLLEGE=log_obj)
    res2 = []
    for stf_obj in stf_obj22:
        print("ss")

        ss = {"status": "ok", 'date': stf_obj.date, 'ename': stf_obj.ename, 'descri': stf_obj.descri,
              'etype': stf_obj.etype, 'id': stf_obj.id}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def usr_view_college_evnt_requst(request):
    if request.method == "POST":
        print("hlw")

        lid = request.POST['lid']
        eid = request.POST['eid']
        log_obj = loginmodel.objects.get(id=lid)
        user_obj = studentmodel.objects.get(LID=log_obj)

        evt_obj = eventmodel.objects.get(id=eid)

        log_obj = participantmodel()
        log_obj.STUDENT = user_obj
        log_obj.EVENT = evt_obj
        log_obj.status = 'pending'

        log_obj.save()

        data = {"status": "ok"}
        return JsonResponse(data)


def usr_view_college_evnt_sts(request):
    lid = request.POST['lid']

    log_obj = loginmodel.objects.get(id=lid)
    user_obj = studentmodel.objects.get(LID=log_obj)
    stf_obj22 = participantmodel.objects.filter(STUDENT=user_obj)

    res2 = []
    for stf_obj in stf_obj22:
        print("ss")

        ss = {"status": "ok", 'event': stf_obj.EVENT.ename, 'status': stf_obj.status}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def usr_view_eorg_evnt(request):
    print("hlw")

    stf_obj22 = event2model.objects.all()
    res2 = []
    for stf_obj in stf_obj22:
        print("ss")

        ss = {"status": "ok", 'date': stf_obj.date, 'ename': stf_obj.ename, 'descri': stf_obj.descri,
              'etype': stf_obj.etype, "id": stf_obj.id}
        print(ss)
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def usr_view_eorg_evnt_requst(request):
    if request.method == "POST":
        print("hlw")

        lid = request.POST['lid']
        eid = request.POST['eid']
        log_obj = loginmodel.objects.get(id=lid)
        user_obj = studentmodel.objects.get(LID=log_obj)

        evt_obj = event2model.objects.get(id=eid)

        log_obj = participantmodel2()
        log_obj.STUDENT = user_obj
        log_obj.EVENT = evt_obj
        log_obj.status = 'pending'

        log_obj.save()

        data = {"status": "ok"}
        return JsonResponse(data)


def usr_view_eorg_evnt_sts(request):
    lid = request.POST['lid']

    log_obj = loginmodel.objects.get(id=lid)
    user_obj = studentmodel.objects.get(LID=log_obj)
    stf_obj22 = participantmodel2.objects.filter(STUDENT=user_obj)

    res2 = []
    for stf_obj in stf_obj22:
        print("ss")

        ss = {"status": "ok", 'event': stf_obj.EVENT.ename, 'status': stf_obj.status}
        res2.append(ss)
    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def portifolio_add(request):
    if request.method == "POST":
        print("hlw")
        ac = request.POST['ac']
        po = request.POST['po']

        lid = request.POST['lid']
        log_obj = loginmodel.objects.get(id=lid)
        user_obj = studentmodel.objects.get(LID=log_obj)

        import datetime
        ddd = datetime.date.today()

        log_obj = portfoliomodel()
        log_obj.achievement = ac
        log_obj.date = ddd
        log_obj.position = po
        log_obj.STUDENT = user_obj

        log_obj.save()

        data = {"status": "ok"}
        return JsonResponse(data)


######jqry........

def ttt(request):
    res = collegemodel.objects.all()

    return render(request, 'college/ttt.html', {'res': res})


def ttt_sub(request):
    print("hh")
    cid = request.GET['clgid']
    print(cid)
    log_obj = collegemodel.objects.get(id=cid)
    print(log_obj)

    stf_obj22 = staffmodel.objects.filter(COLLEGE=log_obj)
    print(stf_obj22)
    res2 = []
    for stf_obj in stf_obj22:
        print("ss")

        ss = {'name': stf_obj.name, 'id': stf_obj.pk}
        res2.append(ss)
    return JsonResponse({'status': 'ok', 'data': res2})


def ttt_pst(request):
    if request.method == "POST":
        print("hlw")
        a = request.POST["select"]
        a1 = request.POST["select2"]
        print("a2=", a1)
        print("a1=", a)

        return render(request, 'college/ttt.html')



        ###ovr


####4  sprint

def eorg_evnt_add(request):
    if request.method == "POST":
        d1 = request.POST['date']
        e1 = request.POST['ename']
        des = request.POST['descri']
        etype = request.POST['etype']
        cid = request.session["lid"]
        log_ob = loginmodel.objects.get(id=cid)
        mmss22 = eventorgizermodel.objects.get(LOGIN=log_ob)

        a1 = event2model(date=d1, descri=des, etype=etype, EVENT_ORG=mmss22, ename=e1)
        a1.save()

        return render(request, "event_orgizr/home.html")
    return render(request, 'event_orgizr/event_add.html')


def eorg_evnt_view(request):
    if request.method == "POST":
        print("qq")
        d1 = request.POST["d1"]
        d2 = request.POST["d2"]
        print("qq")
        cc = event2model.objects.filter(date__gte=d1, date__lte=d2)
        print(cc)
        return render(request, "event_orgizr/event_view.html", {'res': cc})

    print("hlw")
    cid = request.session["lid"]
    print(cid)
    log_ob = loginmodel.objects.get(id=cid)
    mmss22 = eventorgizermodel.objects.get(LOGIN=log_ob)
    print(mmss22)

    res = event2model.objects.filter(EVENT_ORG=mmss22)
    print(res)

    return render(request, "event_orgizr/event_view.html", {'res': res})


def eorg_evnt_edit(request, id):
    res = event2model.objects.get(id=id)
    print(res)
    print("qq")
    request.session["id"] = id

    return render(request, 'event_orgizr/event_edit.html', {'i': res})


@csrf_exempt
def eorg_evnt_post(request):
    id = request.session["id"]
    d1 = request.POST['date']
    e1 = request.POST['ename']
    des = request.POST['descri']
    etype = request.POST['etype']
    cid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=cid)
    mmss22 = eventorgizermodel.objects.get(LOGIN=log_ob)

    res = event2model.objects.get(id=id)

    if request.method == "POST":
        res.date = d1
        res.descri = des
        res.etype = etype
        res.EVENT_ORG = mmss22
        res.ename = e1
        # res.description=dis
        res.save()

        return render(request, "event_orgizr/home.html")
    return render(request, 'event_orgizr/event_edit.html', {'res': res})


def eorg_evnt_del(request, id):
    res = event2model.objects.get(id=id)
    res.delete()
    return render(request, "event_orgizr/home.html")


def clg_cmt_view(request):
    a = request.session["lid"]
    log_ob = loginmodel.objects.get(id=a)
    clg_obj = collegemodel.objects.get(LID=log_ob)
    cmt_obj = complaintmodel.objects.filter(reply='pending')
    res2 = []

    for i in cmt_obj:
        print("kk")

        try:
            print("jj")
            stud_obj = studentmodel.objects.get(id=i.STUDENT_id, COLLEGE=clg_obj)
            print(stud_obj)
            s = {'id': i.id, 'cmt': i.cmt, 'datee': i.datee, 'name': stud_obj.name, 'department': stud_obj.department,
                 'sem': stud_obj.sem}
            print(s)
            res2.append(s)

        except:

            print("qqq")
    print("QQQQQQQQQQ")
    print(res2)
    return render(request, "college/Complaint_view.html", {'res': res2})


def clg_cmt_reply(request, id, cmt):
    request.session["id"] = id

    return render(request, 'college/reply_cmt.html', {'cmt': cmt})


@csrf_exempt
def clg_cmt_preply_post(request):
    id = request.session["id"]

    na1 = request.POST["tt"]

    res = complaintmodel.objects.get(id=id)

    if request.method == "POST":
        res.reply = na1
        # res.description=dis
        res.save()

        return render(request, "college/home.html")
    return render(request, 'college/reply_cmt.html')


def eorg_view_particint(request):
    print("jjj22233")

    a = request.session["lid"]
    log_ob = loginmodel.objects.get(id=a)
    print(log_ob)
    eobj = eventorgizermodel.objects.get(LOGIN=log_ob)
    print(eobj)
    cmt_obj = event2model.objects.filter(EVENT_ORG=eobj)
    print(cmt_obj)
    res2 = []

    for i in cmt_obj:
        print("kk")

        try:
            print("jj22")
            print(i)
            print("______")
            part_obj = participantmodel2.objects.filter(EVENT=i)

            print(part_obj)
            for j in part_obj:
                print("dd")

                s = {'id': j.id, 'event': i.ename, 'name': j.STUDENT.name, 'img': j.STUDENT.img,
                     'phone': j.STUDENT.name, 'email': j.STUDENT.email}
                print(s)
                res2.append(s)

        except:

            print("qqq")
    print("QQQQQQQQQQ")
    print(res2)
    return render(request, "event_orgizr/particent_view.html", {'res': res2})


def eorg_view_particint_approve(request, id):
    part_obj = participantmodel2.objects.get(id=id)
    part_obj.status = 'approved'
    part_obj.save()

    return render(request, 'event_orgizr/home.html')


def eorg_view_particint_reject(request, id):
    part_obj = participantmodel2.objects.get(id=id)
    part_obj.status = 'rejected'
    part_obj.save()

    return render(request, 'event_orgizr/home.html')


#############
def chatload_phy_car(request):
    return render(request, 'carrier/fur_chat.html')


def drviewmsg_phy_car(request, receiverid):
    doclidlid = request.session["lid"]
    print("!!!!!!!!!!", doclidlid, receiverid)
    log_ob = loginmodel.objects.get(id=doclidlid)
    doc = usermodel.objects.get(LOGIN=log_ob)
    print(doc)
    # stud_ob=studentmodel.objects.get(LID=rec)
    lll = loginmodel.objects.get(id=receiverid)
    print("jjj")
    print(lll)
    xx = staffmodel.objects.get(id=receiverid)
    print(xx)
    print("xx ovr")
    obj = chat_staff_phy.objects.filter(FID=xx, UID=doc)
    print(obj)
    user_data = staffmodel.objects.get(id=receiverid)
    print(user_data)
    print("********************", obj)

    res = []
    for i in obj:
        s = {'id': i.pk, 'date': i.date, 'msg': i.message, 'type': i.type}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res, 'name': user_data.name, 'image': user_data.image})


def chatview_phy_car(request):
    print("hai")
    cid = request.session["lid"]
    print(cid)
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = usermodel.objects.get(LOGIN=mmss)
    print(ms)

    da = staffmodel.objects.filter(type='phy')
    print(da)
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.name, 'email': i.email, 'image': i.image}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})


def doctor_insert_chat_phy_car(request, receiverid, msg):
    print("hai riss")

    dlid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=dlid)
    dobj = usermodel.objects.get(LOGIN=log_ob)
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime = datetime.datetime.now()
    print("qqq")
    print(staffmodel.objects.get(pk=receiverid))

    obj = chat_staff_phy()
    obj.FID = staffmodel.objects.get(pk=receiverid)
    obj.UID = dobj
    obj.message = msg
    obj.type = 'user'
    obj.date = showtime
    obj.save()
    print("yyy")
    return JsonResponse({'status': 'ok'})


################ phy-carrior-chat


def chatload_phy_car_to(request):
    return render(request, 'physical/fur_chat_carrior.html')


def drviewmsg_phy_car_to(request, receiverid):
    doclidlid = request.session["lid"]
    print("!!!!!!!!!!", doclidlid, receiverid)
    log_ob = loginmodel.objects.get(id=doclidlid)
    doc = staffmodel.objects.get(LOGIN=log_ob)
    print(doc)
    # stud_ob=studentmodel.objects.get(LID=rec)
    lll = loginmodel.objects.get(id=receiverid)
    print("jjj")
    print(lll)
    xx = usermodel.objects.get(id=receiverid)
    print(xx)
    print("xx ovr")
    obj = chat_staff_phy.objects.filter(FID=doc, UID=xx)
    print(obj)
    user_data = usermodel.objects.get(id=receiverid)
    print(user_data)
    print("********************", obj)

    res = []
    for i in obj:
        s = {'id': i.pk, 'date': i.date, 'msg': i.message, 'type': i.type}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res, 'name': user_data.name, 'image': user_data.image})


def chatview_phy_car_to(request):
    print("hai")
    cid = request.session["lid"]
    print(cid)
    mmss = loginmodel.objects.get(id=cid)
    print(mmss)
    ms = staffmodel.objects.get(LOGIN=mmss)
    print(ms)

    da = usermodel.objects.all()
    print(da)
    res = []
    for i in da:
        s = {'id': i.pk, 'name': i.name, 'email': i.email, 'image': i.image}
        res.append(s)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})


def doctor_insert_chat_phy_car_to(request, receiverid, msg):
    print("hai riss")

    dlid = request.session["lid"]
    log_ob = loginmodel.objects.get(id=dlid)
    dobj = staffmodel.objects.get(LOGIN=log_ob)
    import datetime
    datetime.date.today()  # Returns 2018-01-15
    showtime = datetime.datetime.now()
    print("qqq")
    print(usermodel.objects.get(pk=receiverid))

    obj = chat_staff_phy()
    obj.FID = dobj

    obj.UID = usermodel.objects.get(pk=receiverid)
    obj.message = msg
    obj.type = 'fuser'
    obj.date = showtime
    obj.save()
    print("yyy")
    return JsonResponse({'status': 'ok'})


def clg_assign_view(request):
    print("jj")
    res = assign_cate_model.objects.all()
    print(res)

    return render(request, "college/View_assign_cate.html", {'ii': res})


def clg_assign_del(request, id):
    res = assign_cate_model.objects.get(id=id)
    res.delete()

    return render(request, "college/home.html")


def clg_teammbr_view(request):
    print("jj")
    a = request.session["lid"]
    logobj = loginmodel.objects.get(id=a)
    stf_ob = staffmodel.objects.get(LOGIN=logobj)
    cid = stf_ob.COLLEGE.id
    clg_ob = collegemodel.objects.get(id=cid)
    clg_team_ob = collegeteammodel.objects.filter(COLLEGE=clg_ob)
    res2 = []
    for ii in clg_team_ob:
        print("ii")

        res = team_member_model.objects.filter(TEAM=ii)
        print(res)
        for j in res:
            print("")
            s = {'pk': j.id, 'sname': j.STUDENT.name, 'team': j.TEAM.namee}
            print(s)
            res2.append(s)

    return render(request, "physical/View_team_mbrs.html", {'ii': res2})


def clg_teambr_del(request, id):
    res = team_member_model.objects.get(id=id)
    res.delete()

    return render(request, "physical/home.html")


####
def org_paricipants(request):
    print("hlw")
    cid = request.session["lid"]
    print(cid)
    log_ob = loginmodel.objects.get(id=cid)
    eobj = eventorgizermodel.objects.get(LOGIN=log_ob)

    eventorg = event2model.objects.filter(EVENT_ORG=eobj)
    for jj in eventorg:
        print("jj")
        try:
            print("try")
            mmss22 = studentmodel.objects.all()
            res2 = []
            print(mmss22)
            for i in mmss22:
                print("qqq")

                r4 = participantmodel2.objects.filter(STUDENT=i, status='pending', EVENT=jj)
                for j in r4:
                    ss = {'id': i.pk, 'sname': j.STUDENT.name, 'event': j.EVENT.ename, 'date': j.EVENT.date,
                          'descri': j.EVENT.descri, 'etype': j.EVENT.etype}
                    res2.append(ss)

            return render(request, "college/particpnt_view.html", {'res': res2})

        except:
            print("err")


def org_paricipants_acpt(request):
    print("hlw")
    cid = request.session["lid"]
    print(cid)
    log_ob = loginmodel.objects.get(id=cid)
    clg_og = collegemodel.objects.get(LID=log_ob)
    mmss22 = studentmodel.objects.all()
    res2 = []
    print(mmss22)
    for i in mmss22:
        print("qqq")

        r4 = participantmodel.objects.filter(STUDENT=i, status='accept')
        for j in r4:
            ss = {'id': i.pk, 'sname': j.STUDENT.name, 'event': j.EVENT.ename, 'date': j.EVENT.date,
                  'descri': j.EVENT.descri, 'etype': j.EVENT.etype}
            res2.append(ss)

    return render(request, "college/participant_accpt.html", {'res': res2})


def org_paricipants_accept(request, id):
    print("hlw")
    res = participantmodel.objects.get(id=id)
    res.status = 'accept'
    res.save()
    return render(request, "college/home.html")


def org_paricipants_reject(request, id):
    res = participantmodel.objects.get(id=id)
    res.status = 'reject'
    res.save()
    return render(request, "college/home.html")
