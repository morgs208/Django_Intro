from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("Placeholder to hold future blogs")

def new(request):
    return HttpResponse("Placeholder to display a new for to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"Placeholder to hold blog#{number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to EDIT {number}")

def destroy(request):
    return redirect("/")
