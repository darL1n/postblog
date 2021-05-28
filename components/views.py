from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def cal_date(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Sergey'
    month = month.capitalize()
    # Conver month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # Create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # Get curent year
    now = datetime.now()
    curent_year = now.year
    # Get curent Time
    now = datetime.now()
    curent_time = now.strftime('%a %I:%M %p ')
    #curent_time = now.strftime(' %c ')

    return render(request, 'cal_date.html', {
    'name': name,
    'year': year,
    'month': month,
    'month_number': month_number,
    'cal': cal,
    'curent_year': curent_year,
    'curent_time': curent_time
    })



# Create your views here.
