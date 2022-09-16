from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year, month):
    name = "Elian"
    return render(request, 
    "home.html", {
        "name": name,
        "year": year,
        "month": month, 
    })