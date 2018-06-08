from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import SchedulerForm


# Create your views here.


def scheduler_view(request):
    # Если данный запрос типа POST, тогда
    if request.method == 'POST':
        # Создаем экземпляр формы и заполняем данными из запроса (связывание, binding):
        form = SchedulerForm(request.POST)
        # Проверка валидности данных формы:
        if form.is_valid():
            # Обработка данных из form.cleaned_data
            # (здесь мы просто присваиваем их полю due_back)
            # book_inst.due_back = form.cleaned_data['renewal_date']
            # book_inst.save()
            form.save()
            # Переход по адресу 'all-borrowed':
            return HttpResponseRedirect(reverse('main'))
    # Если это GET (или какой-либо еще), создать форму по умолчанию.
    else:
        form = SchedulerForm()

    return render(request, 'scheduler/scheduler.html', {'form': form})


class Scheduler_add(CreateView):
    success_url = '/'
    form_class = SchedulerForm
    template_name = 'scheduler/scheduler.html'
