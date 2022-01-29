from django.views.generic.list import ListView
from .models import Expense


class IndexView(ListView):
    template_name = 'expenses/index.html'
    context_object_name = 'expenses'
    model = Expense
    ordering = ['date']