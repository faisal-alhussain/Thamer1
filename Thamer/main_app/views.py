
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login, logout
from .models import Company,Review, User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/users/login/")

def add_company(request:HttpRequest):

    if request.method == "POST":
        # Adding a new company to the database
        new_company = Company(
            name=request.POST["name"],
            description=request.POST["description"],
            local_score=request.POST["local_score"],
            ikteva_score_now=request.POST["ikteva_score_now"],
            ikteva_score_before=request.POST["ikteva_score_before"],
            email=request.POST["email"],
            contact_number=request.POST["contact_number"],
            sectors=request.POST["sectors"],
            owner=request.user  
                        
            )
        
        new_company.save()
        return redirect("main_app:market_page")

    return render(request, "main_app/add_company.html")


def market_page(request:HttpRequest):

    #Show all data inside the model in MArket

        
    companys = Company.objects.all()


    return render(request, "main_app/market.html",  {"companys" : companys})





def company_detail(request:HttpRequest, company_id):

        #Show each  data inside the model in thier ID


    company = Company.objects.get(id=company_id)

    return render(request, 'main_app/company_detail.html', {"company" : company}) 


@login_required(login_url="/users/login/")
def update_company(request:HttpRequest, company_id):

    company = Company.objects.get(id=company_id)

    #updating the Company model
    if request.method == "POST":
        company.name=request.POST["name"]
        company.description = request.POST["description"]
        company.local_score=request.POST["local_score"]
        company.ikteva_score_now=request.POST["ikteva_score_now"]
        company.ikteva_score_before=request.POST["ikteva_score_before"]
        company.email=request.POST["email"]
        company.contact_number =request.POST["contact_number"]
        company.twitter_link = request.POST["twitter_link"]
        company.website = request.POST["website"]
        company.instagram_link = request.POST["instagram_link"]



        company.save()

        return redirect("main_app:company_detail", company_id=company.id)

    return render(request, 'main_app/update_company.html', {"company" : company})

@login_required(login_url="/users/login/")
def delete_company(request:HttpRequest, company_id):

    #Delete the company from the model 
    
    company = Company.objects.get(id=company_id)
    company.delete()

    return redirect("main_app:market_page")




def about_us(request:HttpRequest):
    
# About us HTML
    return render(request, "main_app/about_us.html")




def ikteva_page(request:HttpRequest):
    
# ikteva HTML

    return render(request, "main_app/ikteva_page.html")



def index_page(request:HttpRequest):
    
# Home HTML

    return render(request, "main_app/index.html")



# Future feature

def add_review(request:HttpRequest, company_id):

    if request.method == "POST":
        company_object = Company.objects.get(id=company_id)
        new_review = Review(company=company_object, user=request.user, content=request.POST["content"], rating=request.POST["rating"])
        new_review.save()

    
    return redirect("main_app:company_detail", company_id=company_id)



def payment_page(request:HttpRequest):
    
    # payment page HTML

    return render(request, "main_app/payment_page.html")



def experts_page(request:HttpRequest):

    # payment page HTML


    return render(request, "main_app/experts_page.html")

@login_required(login_url="/users/login/")
def company_page(request:HttpRequest):
    # Retrieve companies associated with the currently logged-in user
    company = Company.objects.filter(owner=request.user)

    # Pass the companies variable to the template in the context dictionary
    return render(request, "main_app/my_compnies.html", {"company": company})




def onwer_details(request:HttpRequest, company_id):

        #Show each  data inside the model in thier ID


    company = Company.objects.get(id=company_id)

    return render(request, 'main_app/onwer_details.html', {"company" : company}) 







# Create your views here.
def signup(request: HttpRequest):
    if request.method == "POST":
        print(request.POST["phone"])
        try:
            new_user = User.objects.create_user(
                username=request.POST["user_name"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            new_user.save()
            profile = Profile(user=new_user, phone_number=request.POST["phone"])
            profile.save()
            profile.save()
            group = Group.objects.get(name="customers")
            request.user.groups.add(group)
            return redirect("main_app:index_page")
        except:
            print("error")
            msg = "Username taken!"
    return render(request, "main_app/login.html")


def login_page(request: HttpRequest):
    if request.user.is_authenticated:
        print(request.user.username)
        return redirect("main_app:index")
    # if user login already redirect to home page

    msg = None
    if request.method == "POST":
        user: User = authenticate(
            request,
            username=request.POST["user_name"],
            password=request.POST["password"],
        )
        if user:
            login(request, user)
            return redirect("main_app:index_page")
        else:
            msg = "Incorrect Credentials"

    return render(request, "main_app/login.html", {"msg": msg})


def signout_page(request: HttpRequest):
    logout(request)

    return redirect("main_app:index_page")


def no_permission_page(request: HttpRequest):
    return render(request, "main_app/no_permission.html")



