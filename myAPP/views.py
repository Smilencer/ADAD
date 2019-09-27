from django.shortcuts import render
from django.http import JsonResponse
from myAPP.models import login_info, patient_info, symptom_info, moca_info
import uuid
from datetime import date
import base64
import json


def index(request):
    return render(request, "index.html")


def handleRequest(request):
    feedback = None
    if request.is_ajax():
        if request.POST.get("cmd", None) == "signin":
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            try:
                userObj = login_info.objects.get(username=username, password=password)
                feedback = {"userID": userObj.userID}
            except:
                feedback = {"userID": None}
        if request.POST.get("cmd", None) == "signup":
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            try:
                uniqueID = uuid.uuid4()
                userObj = login_info(userID=uniqueID, username=username, password=password)
                userObj.save()
                feedback = {"userID": uniqueID}
            except:
                feedback = {"userID": None}
        if request.POST.get("cmd", None) == "personal":
            userID = request.POST.get("userID", None)
            fullname = request.POST.get("fullname", None)
            gender = request.POST.get("gender", None)
            birthday = request.POST.get("birthday", None)
            marriage = request.POST.get("marriage", None)
            phone = request.POST.get("phone", None)
            history = request.POST.get("history", None)
            address = request.POST.get("address", None)
            ename = request.POST.get("ename", None)
            ephone = request.POST.get("ephone", None)
            try:
                history_bool = False
                if history == "on":
                    history_bool = True
                marriage_bool = False
                if marriage == "true":
                    marriage_bool = True
                birth_date = birthday.split("-")
                userObj = login_info.objects.get(userID=userID)
                obj, created = patient_info.objects.update_or_create(user=userObj,
                                                                     defaults={'name': fullname,
                                                                               'gender': gender,
                                                                               'birthday': date(int(birth_date[0], 10),
                                                                                                int(birth_date[1], 10),
                                                                                                int(birth_date[2], 10)),
                                                                               'marriage': marriage_bool,
                                                                               'phone': phone, 'history': history_bool,
                                                                               'address': address,
                                                                               'emergency_name': ename,
                                                                               'emergency_phone': ephone})
                feedback = {"userID": userID}
            except Exception as e:
                print(e)
                feedback = {"userID": None}
        if request.POST.get("cmd", None) == "symtom":
            userID = request.POST.get("userID", None)
            adtype = request.POST.get("adtype", None)
            symptom = request.POST.get("sympton", None)
            description = request.POST.get("description", None)
            userObj = login_info.objects.get(userID=userID)
            obj, created = symptom_info.objects.update_or_create(user=userObj,
                                                                 defaults={'type': adtype, 'symptom': symptom,
                                                                           'description': description})
            feedback = {"userID": userID}
        if request.POST.get("cmd", None) == 'Q1-1':
            mocaID = request.POST.get("mocaID", None)
            sketch = request.POST.get("sketch", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_1_1 = sketch
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q1-2':
            mocaID = request.POST.get("mocaID", None)
            sketch = request.POST.get("sketch", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_1_2 = sketch
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q1-3':
            mocaID = request.POST.get("mocaID", None)
            sketch = request.POST.get("sketch", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_1_3 = sketch
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q2-1':
            mocaID = request.POST.get("mocaID", None)
            animal = request.POST.get("animal", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_2_1 = animal
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q2-2':
            mocaID = request.POST.get("mocaID", None)
            animal = request.POST.get("animal", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_2_2 = animal
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q2-3':
            mocaID = request.POST.get("mocaID", None)
            animal = request.POST.get("animal", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_2_3 = animal
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q3-1':
            mocaID = request.POST.get("mocaID", None)
            audio = request.POST.get("audio", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_3_1 = audio
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q4-1':
            mocaID = request.POST.get("mocaID", None)
            audio = request.POST.get("audio", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_4_1 = audio
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q4-2':
            mocaID = request.POST.get("mocaID", None)
            audio = request.POST.get("audio", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_4_2 = audio
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q4-3':
            mocaID = request.POST.get("mocaID", None)
            taps = request.POST.get("taps", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_4_3 = taps
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q4-4':
            mocaID = request.POST.get("mocaID", None)
            results = request.POST.get("results", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_4_4 = results
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q5-1':
            mocaID = request.POST.get("mocaID", None)
            audio = request.POST.get("audio", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_5_1 = audio
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q5-2':
            mocaID = request.POST.get("mocaID", None)
            audio = request.POST.get("audio", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_5_2 = audio
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q5-3':
            mocaID = request.POST.get("mocaID", None)
            audio = request.POST.get("audio", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_5_3 = audio
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q6-1':
            mocaID = request.POST.get("mocaID", None)
            results = request.POST.get("results", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_6_1 = results
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q3-2-2':
            mocaID = request.POST.get("mocaID", None)
            audio = request.POST.get("audio", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_3_2_2 = audio
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q3-2-1':
            mocaID = request.POST.get("mocaID", None)
            results = request.POST.get("results", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_3_2_1 = results
            mocaObj.save()
            feedback = {"success": "ok"}
        if request.POST.get("cmd", None) == 'Q7-1':
            mocaID = request.POST.get("mocaID", None)
            results = request.POST.get("results", None)
            mocaObj = moca_info.objects.get(mocaID=mocaID)
            mocaObj.question_7_1 = results
            mocaObj.save()
            feedback = {"success": "ok", "userID": mocaObj.user_id}
    return JsonResponse(feedback, safe=False)


def patient(request):
    feedback = None
    if request.method == "GET":
        userID = request.GET.get("userID", None)
        try:
            userObj = login_info.objects.get(userID=userID)
            patientObj = patient_info.objects.get(user=userObj)
            feedback = {"userID": userID, "patientObj": patientObj,
                        "birth_date": patientObj.birthday.strftime("%Y-%m-%d")}
        except:
            feedback = {"userID": userID}
        return render(request, "patient.html", feedback)


def symptom(request):
    feedback = None
    if request.method == "GET":
        userID = request.GET.get("userID", None)
        try:
            userObj = login_info.objects.get(userID=userID)
            symptomObj = symptom_info.objects.get(user=userObj)
            symptomArray = symptomObj.symptom.split(',')
            symptomMap = {}
            for sym in symptomArray:
                symptomMap[sym] = sym
            feedback = {"userID": userID, "type": symptomObj.type,
                        "description": symptomObj.description}
            feedback.update(symptomMap)
        except:
            feedback = {"userID": userID}
    return render(request, "symptom.html", feedback)


def menu(request):
    return render(request, "menu.html")


def mri(request):
    feedback = None
    if request.method == "GET":
        userID = request.GET.get("userID", None)
        try:
            userObj = login_info.objects.get(userID=userID)
            patientObj = patient_info.objects.get(user=userObj)
            birthday = patientObj.birthday
            today = date.today()
            age = today.year - birthday.year
            feedback = {"userID": userID, "age": age,
                        "gender": patientObj.gender}
        except:
            feedback = {"userID": userID}
    return render(request, "mri.html", feedback)


def report(request):
    feedback = None
    if request.method == "GET":
        userID = request.GET.get("userID", None)
        try:
            userObj = login_info.objects.get(userID=userID)
            patientObj = patient_info.objects.get(user=userObj)
            birthday = patientObj.birthday
            today = date.today()
            age = today.year - birthday.year
            feedback = {"userID": userID, "age": age,
                        "gender": patientObj.gender}
        except:
            feedback = {"userID": userID}
    return render(request, "report.html", feedback)


def indice(request):
    feedback = None
    if request.method == "GET":
        userID = request.GET.get("userID", None)
        try:
            userObj = login_info.objects.get(userID=userID)
            patientObj = patient_info.objects.get(user=userObj)
            birthday = patientObj.birthday
            today = date.today()
            age = today.year - birthday.year
            feedback = {"userID": userID, "age": age,
                        "gender": patientObj.gender}
        except:
            feedback = {"userID": userID}
    return render(request, "indice.html", feedback)


def indice2(request):
    feedback = None
    if request.method == "GET":
        userID = request.GET.get("userID", None)
        try:
            userObj = login_info.objects.get(userID=userID)
            patientObj = patient_info.objects.get(user=userObj)
            birthday = patientObj.birthday
            today = date.today()
            age = today.year - birthday.year
            feedback = {"userID": userID, "age": age,
                        "gender": patientObj.gender}
        except:
            feedback = {"userID": userID}
    return render(request, "indice2.html", feedback)


def help_diagnosis_AD_imgs(request):
    result = 'error'
    if request.method == "POST":
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        age = int(age)
        if gender == 'M':
            gender = int(1)
        else:
            gender = int(0)
        data = request.POST.get("data_result")
        data = json.loads(data)[0]
        print(data)
        img1_str = request.POST.get("img1")
        img2_str = request.POST.get("img2")
        img3_str = request.POST.get("img3")
        if img1_str != '':
            img1_base64 = base64.b64decode(img1_str)
            img_fileroad = r'static/ad_imgs'
            print(img_fileroad)
            file = open(img_fileroad + r'/img1.jpg', 'wb')
            file.write(img1_base64)
            file.close()
        if img2_str != '':
            img2_base64 = base64.b64decode(img2_str)
            img_fileroad = r'static/ad_imgs'
            file = open(img_fileroad + r'/img2.jpg', 'wb')
            file.write(img2_base64)
            file.close()
        if img3_str != '':
            img3_base64 = base64.b64decode(img3_str)
            img_fileroad = r'static/ad_imgs'
            file = open(img_fileroad + r'/img3.jpg', 'wb')
            file.write(img3_base64)
            file.close()
        from core.ad_model.imgs.runmodel import model_predict
        input_data = [[]]
        input_data[0].append(float(data['tau']))
        input_data[0].append(float(data['ptau']))
        input_data[0].append(float(data['abeta40']))
        input_data[0].append(float(data['abeta42']))
        input_data[0].append(age)
        input_data[0].append(gender)
        input_data[0].append(float(data['apoe']))
        input_data[0].append(float(data['cdr']))
        input_data[0].append(float(data['mmse']))
        input_data[0].append(float(data['ravlt']))
        input_data[0].append(float(data['faq']))
        print('input', input_data)
        result = model_predict('', input_data)
        # result= 'true'
    return JsonResponse(result, safe=False)


def help_diagnosis_AD_text(request):
    result = 'error'
    if request.method == "POST":
        # gender = request.POST.get("gender")
        # age = request.POST.get("age")
        text = request.POST.get("text")
        from core.ad_model.text.predict_new import diagnosis_AD_text
        result = diagnosis_AD_text(text)
    return JsonResponse(result, safe=False)


def help_diagnosis_AD_index(request):
    result = 'error'
    if request.method == "POST":
        gender = request.POST.get("gender")
        sex_index = 1
        if gender == 'M':
            sex_index = 0
        age = request.POST.get("age")
        data = request.POST.get("data_result")
        data = json.loads(data)
        print(data[0])
        test = [[]]
        temp = []
        for k in range(0, 3):
            temp.append(int(age))
            temp.append(sex_index)
            base = 4
            for i in range(0, 5):
                index_AD = str(base + i + k * 5)
                # print(index_AD)
                print(data[0][index_AD])
                temp.append(float(data[0][index_AD]))
            print(temp)
            test[0].append(temp)
            temp = []
            base += 4
        print(test)
        from core.ad_model.index.example import diagnosis_AD_index
        result = diagnosis_AD_index(test)
    return JsonResponse(result, safe=False)


def help_predict_AD_index(request):
    result = 'error'
    if request.method == "POST":
        data = json.loads(request.POST.get("dataJSON"))
        import pandas as pd
        DataTest = pd.DataFrame(data)
        from core.ad_model.index2.predict import predict_AD_index
        result = predict_AD_index(DataTest)
    return JsonResponse(result, safe=False)


def moca(request):
    if request.method == "GET":
        feedback = {"hrefNext": "#"}
        pageList = ["1-1", "1-2", "1-3", "2-1", "2-2", "2-3", "3-1", "4-1", "4-2", "4-3", "4-4", "5-1", "5-2", "5-3",
                    "6-1", "3-2", "7-1"]
        version = request.GET.get("v", None)
        feedback["version"] = version
        question = request.GET.get("q", None)
        qIndex = pageList.index(question)
        if (qIndex == 0):
            userID = request.GET.get("userID", None);
            mocaID = uuid.uuid4()
            userObj = login_info.objects.get(userID=userID)
            mocaObj = moca_info(user=userObj, mocaID=mocaID, version=version)
            mocaObj.save()
        else:
            mocaID = request.GET.get("mocaID", None);
        feedback["mocaID"] = mocaID
        if (qIndex < len(pageList) - 1):
            qNext = pageList[qIndex + 1]
            hrefNext = "/moca/?v=" + version + "&q=" + qNext + "&mocaID=" + str(mocaID)
            feedback["hrefNext"] = hrefNext
        return render(request, "moca/Q" + question + ".html", feedback)
