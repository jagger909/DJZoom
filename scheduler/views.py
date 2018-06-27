import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import SchedulerForm
from .models import Scheduler


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


class SchedulerView(CreateView):
    success_url = reverse_lazy('scheduler_index')
    form_class = SchedulerForm
    template_name = 'scheduler/scheduler2.html'


def scheduler_free_time(request):
    # try:
    #     rep_date = request.GET["rep_date"]
    # except KeyError:
    #     rep_date = datetime.date.today()

    rep_date = datetime.datetime.strptime('09-06-2018', "%d-%m-%Y")
    num_days = 5
    filtered_sched = Scheduler.objects.filter(repair_date__range=(rep_date, rep_date + datetime.timedelta(days=num_days)))
    date_list = [rep_date + datetime.timedelta(days=x) for x in range(0, num_days)]
    events = {}
    for date in date_list:
        busy_time = []
        date_time_list = {choices.name: choices.value for choices in Scheduler.TimeChoice}
        date_busy_time = filtered_sched.filter(repair_date=date)
        for time in date_busy_time:
            busy_time.append(time.repair_time)

        if busy_time:
            for time in busy_time:
                date_time_list.pop(time)
        events[date.strftime('%d-%m-%Y')] = date_time_list
    output = {}
    output["busy_times"] = events

    return JsonResponse(output)


def scheduler_add(request):
    if request.method == 'POST':
        post_username = request.POST.get('post_username')
        post_address = request.POST.get('post_address')
        post_telephone = request.POST.get('post_telephone')
        post_comment = request.POST.get('post_comment')
        post_repair_date = request.POST.get('post_repair_date')
        post_repair_time = request.POST.get('post_repair_time')

        response_data = {}

        sched = Scheduler(username=post_username,
                          address=post_address,
                          telephone=post_telephone,
                          comment=post_comment,
                          repair_date=post_repair_date,
                          repair_time=post_repair_time)
        sched.save()

        response_data['result'] = 'Create post successful!'
        response_data['username'] = post_username
        response_data['address'] = post_address
        response_data['telephone'] = post_telephone
        response_data['comment'] = post_comment
        response_data['rep_date'] = post_repair_date
        response_data['rep_time'] = post_repair_time

        return JsonResponse(response_data)

    else:

        return JsonResponse({"nothing to see": "this isn't happening"})
