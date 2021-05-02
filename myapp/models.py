from django.db import models
class loginmodel(models.Model):
    uname=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    class Meta:
        db_table="login"





class collegemodel(models.Model):
    LID=models.ForeignKey(loginmodel,on_delete=models.CASCADE,)
    name=models.CharField(max_length=50)
    img=models.CharField(max_length=250)
    ext_year = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=40)

    class Meta:
        db_table="college"

class studentmodel(models.Model):
    LID = models.ForeignKey(loginmodel, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    house = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    dob=models.CharField(max_length=40)

    department = models.CharField(max_length=50)
    sem = models.CharField(max_length=50)
    gen = models.CharField(max_length=50)
    COLLEGE = models.ForeignKey(collegemodel,on_delete=models.CASCADE,)

    class Meta:
        db_table = "student"


class notificationmodel(models.Model):
    msg = models.CharField(max_length=50)
    datee = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    class Meta:
        db_table="notification"
class sports_catmodel(models.Model):

    name=models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    class Meta:
        db_table="sports_cate"
class sports_profilemodel(models.Model):
    STUDENT = models.ForeignKey(studentmodel, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    class Meta:
        db_table = "sports_profile"


class staffmodel(models.Model):
    LOGIN = models.ForeignKey(loginmodel, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    gen = models.CharField(max_length=50)
    place = models.CharField(max_length=250)
    COLLEGE = models.ForeignKey(collegemodel, on_delete=models.CASCADE, )
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    email = models.CharField(max_length=50)

    class Meta:
        db_table = "staff"


class assign_cate_model(models.Model):
    SPORTS_CATE = models.ForeignKey(sports_catmodel, on_delete=models.CASCADE, )
    STAFF = models.ForeignKey(staffmodel, on_delete=models.CASCADE, )

    date = models.CharField(max_length=50)
    class Meta:
        db_table = "assign_cat"


class motivationmodel(models.Model):
    path=models.CharField(max_length=250)
    date=models.CharField(max_length=50)
    contnt_type = models.CharField(max_length=50)
    desci = models.CharField(max_length=250)
    STAFF = models.ForeignKey(staffmodel, on_delete=models.CASCADE, )
    class Meta:
        db_table="motivation"

class complaintmodel(models.Model):
    STUDENT = models.ForeignKey(studentmodel, on_delete=models.CASCADE, )
    cmt = models.CharField(max_length=250)
    datee = models.CharField(max_length=50)
    reply = models.CharField(max_length=250)

    class Meta:
        db_table = "complaint"


class collegeteammodel(models.Model):
    STAFF = models.ForeignKey(staffmodel, on_delete=models.CASCADE, )
    COLLEGE = models.ForeignKey(collegemodel, on_delete=models.CASCADE, )
    namee = models.CharField(max_length=50)
    datee = models.CharField(max_length=50)
    class Meta:
        db_table = "collegeteam"

class team_member_model(models.Model):
    STUDENT = models.ForeignKey(studentmodel, on_delete=models.CASCADE, )
    TEAM = models.ForeignKey(collegeteammodel, on_delete=models.CASCADE, )

    class Meta:
        db_table = "team_member"

class schedulemodel(models.Model):
    COLLEGETEAM = models.ForeignKey(collegeteammodel, on_delete=models.CASCADE, )

    time_from = models.CharField(max_length=50)
    time_to = models.CharField(max_length=50)
    datee = models.CharField(max_length=50)
    class Meta:
        db_table = "schedule"

class eventmodel(models.Model):

    date = models.CharField(max_length=50)
    ename = models.CharField(max_length=50)
    descri = models.CharField(max_length=250)
    etype = models.CharField(max_length=250)
    COLLEGE=models.ForeignKey(collegemodel, on_delete=models.CASCADE, )

    class Meta:
        db_table = "event"




class participantmodel(models.Model):
    STUDENT = models.ForeignKey(studentmodel, on_delete=models.CASCADE, )
    EVENT = models.ForeignKey(eventmodel, on_delete=models.CASCADE, )

    class Meta:
        db_table = "participant"
####################
class usermodel(models.Model):
    LOGIN = models.ForeignKey(loginmodel, on_delete=models.CASCADE, )
    cname = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    ph = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    details = models.CharField(max_length=250)
    COLLEGE = models.ForeignKey(collegemodel, on_delete=models.CASCADE, )
    desi = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

    name = models.CharField(max_length=50)
    status=models.CharField(max_length=50)

    class Meta:
        db_table = "user"


class gallerymodel(models.Model):
    STAFF = models.ForeignKey(staffmodel, on_delete=models.CASCADE, )
    EVENT = models.ForeignKey(eventmodel, on_delete=models.CASCADE, )

    img = models.CharField(max_length=250)
    datee = models.CharField(max_length=20)
    desi = models.CharField(max_length=50)

    class Meta:
        db_table = "gallery"

class nutritionmodel(models.Model):
    CLG = models.ForeignKey(collegemodel, on_delete=models.CASCADE, )

    name = models.CharField(max_length=50)
    descri = models.CharField(max_length=250)

    class Meta:
        db_table = "nutrition"



class nutritionallocationmodel(models.Model):
    STUDENT = models.ForeignKey(studentmodel, on_delete=models.CASCADE, )
    NUTRITION = models.ForeignKey(nutritionmodel, on_delete=models.CASCADE, )

    quantity = models.CharField(max_length=50)
    datee = models.CharField(max_length=50)

    class Meta:
        db_table = "nutrition_allocation"

class msg_nutitionnist_model(models.Model):
    NUTRITION = models.ForeignKey(nutritionmodel, on_delete=models.CASCADE, )

    datee = models.CharField(max_length=50)
    msg = models.CharField(max_length=250)
    mtype = models.CharField(max_length=50)

    class Meta:
        db_table = "msg_nutitionist"

class chat(models.Model):
    message = models.CharField(max_length=300)
    date = models.CharField(max_length=100)
    type =  models.CharField(max_length=100)
    FID = models.ForeignKey(staffmodel, on_delete=models.CASCADE)
    UID=models.ForeignKey(studentmodel, on_delete=models.CASCADE)

    class Meta:
        db_table = "chatuser"


class eventorgizermodel(models.Model):
    LOGIN = models.ForeignKey(loginmodel, on_delete=models.CASCADE, )
    image = models.CharField(max_length=250)
    ph = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    details = models.CharField(max_length=250)
    desi = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    status=models.CharField(max_length=50)

    class Meta:
        db_table = "event_orgizer"
