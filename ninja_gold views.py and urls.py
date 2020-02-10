import datetime
import random
from django.shortcuts import render, redirect

timestamp = datetime
def index(request):
    if not "gold" in request.session:
        request.session["gold"] = 0
    if not "activity" in request.session:
        request.session["activity"] = []
    
    return render(request,"index.html")

def process_money(request):
    earned = random.randrange(10,20)
    if request.POST["click_coming_from"] == "f_arm":
         request.session["gold"] += earned
         print("You got this much from the farm:")
         print(earned)
         print("Your total is now:")
         print(request.session["gold"])
         

     
    if request.POST["click_coming_from"] == "c_ave":
        request.session["gold"] += random.randrange(5,10)
        print("You got this much from the cave:")
        print(earned)
        print("Your total is now:")
        print(request.session["gold"])
    
    
    if request.POST["click_coming_from"] == "h_ouse":
        request.session["gold"] += random.randrange(2,5)
        print("You got this much from the house:")
        print(earned)
        print("Your total is now:")
        print(request.session["gold"])
     
    if request.POST["click_coming_from"] == "c_asino":
        request.session["gold"] += random.randrange(-50, 50)
        print("You got this much from the casino.....or lost:")
        print(earned)
        print("Your total is now:")
        print(request.session["gold"])

    return redirect("/")
    
