from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import *

import joblib
from datetime import datetime

from django.views.generic.list import ListView


# Create your views here.

def result(request):
    informs = date_input.objects.all().order_by('-input_index')[:1]
    informs_instance = informs.get()
    year = informs_instance.year
    mon = informs_instance.mon
    day = informs_instance.day

    date = datetime(year, mon, day)
    now = datetime.now()
    TimeInterval = date - now
    predict_date = TimeInterval.days

    predict_model = joblib.load('/Users/minbyeongkim/PycharmProjects/Finance/finance/arima_finance.model')
    tem = predict_model.forecast(predict_date)
    price = tem[0][-1]

    return render(request, 'finance/result.html', {'informs':informs, 'price':price})

class predict(CreateView):
    model = date_input
    fields = ['year', 'mon', 'day']
    template_name = 'finance/predict.html'
    def form_valid(self, form):
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})

# def list(request):
#     try:
#         search_option = request.POST["search_option"]
#     except:
#         search_option = "all"
#     try:
#         search = request.POST["search"]
#     except:
#         search = ""
#     try:
#         start = int(request.GET['start'])
#     except:
#         start = 0
#
#     if search_option == "all":
#         list = Aapl.objects.all()
#     elif search_option == "date":
#         list = Aapl.objects.filter(date__contains=search)[:]
#     else:
#         list = Aapl.objects.all()
#
#     # Aapl_list = Aapl.objects
#     paginator = Paginator(list, 15)
#     page = request.GET.get('page')
#     posts = paginator.get_page(page)
#
#     return render(request, 'finance/apple_list.html', {'list':list, 'search_option':search_option, 'search':search,  'posts':posts})

class ListView(ListView):
    model = Apple
    paginate_by = 15