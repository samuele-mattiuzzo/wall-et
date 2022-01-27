from django.http import HttpResponse
from django.shortcuts import render

from .models import Expense


def index(request):
    expenses = Expense.objects.order_by('date')
    context = {'expenses': expenses}
    return render(request, 'expenses/index.html', context)
