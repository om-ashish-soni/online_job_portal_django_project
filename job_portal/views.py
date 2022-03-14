from pickle import FALSE
from django.http import JsonResponse
from django.shortcuts import render, redirect,HttpResponse
from .models import User,Application,Applicant
from django.db import connection

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def signin(request):
    return render(request,'signin.html')

def login(request):
    return render(request,'login.html')
def confirmation(request):
    data=request.session['data']
    return render(request,'confirmation.html',data)
def hrhome(request):
    data=request.session['data']
    return render(request,'hrhome.html',data)
def candidatehome(request):
    data=request.session['data']
    return render(request,'candidatehome.html',data)
def craftApplication(request):
    data=request.session['data']
    return render(request,'craftApplication.html',data)
def readApplication(request,appid):
    
    application=Application.objects.get(appid=appid)
    print("application by hr : ",application.hremail)
    return render(request,'readApplication.html',{
        "application":application
    })
def applyApplication(request,appid):
    email=request.session['data']['email']
    application=Application.objects.get(appid=appid)
    print("application by hr : ",application.hremail)
    return render(request,'applyApplication.html',{
        'email':email,
        "application":application
    })
def appliedApplications(request,candidateemail):
    email=request.session['data']['email']
    myappliedapps=list(Applicant.objects.filter(candidateemail=candidateemail))
    appliedAppList=[]
    for app in myappliedapps:
        appliedAppList.append((app.applicantid,Application.objects.get(appid=app.appid)))
    print("total applied apps by candidate : ",appliedAppList)
    return render(request,'seeAppliedApplications.html',{
        'email':email,
        'appliedAppList':appliedAppList
    })
    pass
def checkAppliedApp(request,applicantid):
    email=request.session['data']['email']
    appliedApp=Applicant.objects.get(applicantid=applicantid)
    print("applied app : ",appliedApp)
    return render(request,'checkAppliedApp.html',{
        'email':email,
        'appliedApp':appliedApp
    })
def getMyApplications(request,hremail):
    myapps=list(Application.objects.filter(hremail=hremail))
    print("total apps by hr : ",len(myapps))
    return render(request,'seeApplicationList.html',{
        'email':hremail,
        'appList':myapps
    })
    pass
def searchJob(request):
    data=request.session['data']
    request.session['data']=data
    return render(request,'searchJobPage.html',{
        'email':data['email']
    })
def checkApplicants(request,appid):
    applicants=list(Applicant.objects.filter(appid=appid))
    print("applicants of app : ",applicants)
    return render(request,'checkApplicants.html',{
        'applicants':applicants
    })
    pass

def lookApplicant(request,applicantid):
    applicant=Applicant.objects.get(applicantid=applicantid)
    print("applicant with given applicant id : ",applicant)
    return render(request,'lookApplicant.html',{
        'applicant':applicant
    })
    pass
def shortlistCandidate(request,applicantid):
    applicant = Applicant.objects.get(applicantid=applicantid)
    Applicant.objects.filter(applicantid=applicantid).update(progress='shortlisted')
    print("candidate to be shortlisted is : ",applicant)
    data=request.session['data']
    data['confirmation_msg']="shortlisted candidate successfully"
    request.session['data']=data
    return redirect('/confirmation')
    pass
def addApplicant(request):
    candidateemail=request.POST.get('candidateemail')
    appid=request.POST.get('appid')
    age=request.POST.get('age')
    location=request.POST.get('location')
    birthdate=request.POST.get('birthdate')
    expected_salary=request.POST.get('expected_salary')
    resume_url=request.POST.get('resume_url')
    progress="pending"
    new_applicant=Applicant.objects.create(
        candidateemail=candidateemail,
        appid=appid,
        age=age,
        location=location,
        birthdate=birthdate,
        expected_salary=expected_salary,
        resume_url=resume_url,
        progress=progress
    )
    new_applicant.save()
    print("saved : ",new_applicant.applicantid)
    data=request.session['data']
    data['confirmation_msg'] = "applied for job successfully"
    request.session['data']=data
    return redirect('/'+'confirmation')
    pass
def postApplication(request):
    data=request.session['data']
    company=request.POST.get('company')
    hremail=request.POST.get('hremail')
    jobtitle=request.POST.get('jobtitle')
    jobfunction=request.POST.get('jobfunction')
    location=request.POST.get('location')
    description=request.POST.get('description')
    salary=request.POST.get('salary')
    new_application=Application.objects.create(
        company=company,
        hremail=hremail,
        jobtitle=jobtitle,
        jobfunction=jobfunction,
        location=location,
        description=description,
        salary=salary
    )
    new_application.save()
    print("saved",new_application.appid)
    return redirect('/'+'readApplication'+'/'+str(new_application.appid))
    # data['confirmation_msg']="posted application successfully"
    # request.session['data']=data
    # return redirect('/confirmation')
def validateSignin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        isHr=request.POST.get('isHr')
        new_user=User.objects.create(
            email=email, password=password, isHr=isHr
        )
        new_user.save()
        destination='login'
        if isHr=="1": destination='hrhome'
        else : destination='candidatehome'
        data=request.session['data']
        data={
            'email':email,
            'isHr':isHr
        }
        request.session['data']=data
        return redirect('/'+destination)
def validateLogin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        isHr=request.POST.get('isHr')
        existingUsers=User.objects.filter(email=email).filter(isHr=isHr).filter(password=password).count()
        destination='login'
        if isHr=="1": destination='hrhome'
        else : destination='candidatehome'
        if existingUsers>0:
            data=request.session['data']
            data={
                'email':email,
                'isHr':isHr
            }
            request.session['data']=data
            return redirect('/'+destination)
        return redirect('/'+destination)
def searchJobApplication(request):
    searchResults=[]
    email=request.session['data']['email']
    if request.method == 'POST':
        company=request.POST.get('company')
        jobtitle=request.POST.get('jobtitle')
        jobfunction=request.POST.get('jobfunction')
        print(company,jobtitle,jobfunction)
        sr1=[];sr2=[];sr3=[]
        sr1=list(Application.objects.filter(company=company))
        sr2=list(Application.objects.filter(jobtitle=jobtitle))
        sr3=list(Application.objects.filter(jobfunction=jobfunction))
        searchResults=sr1+sr2+sr3
        print(searchResults)
    return render(request,'searchJobPage.html',{
        'email':email,
        'searchResults':searchResults,
    })
        