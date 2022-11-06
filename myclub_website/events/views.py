from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

#def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
def home(request, year, month):
    name = "Elian"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    tc = calendar.HTMLCalendar()
    cal = tc.formatmonth(year,month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime("%I:%M: %p")
    
    #return render(request, "events/home.html", {
    return render(request, "home.html", {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
        })