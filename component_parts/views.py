from random import randint

from django.shortcuts import render, redirect
from component_parts import functions_1
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
from .forms import CaseForm


def index(request):
    return render(request, 'component_parts/startpage/startpage.html')


def cases(request):
    case = models.Case.objects.get(id=1)
    model_player_action = models.PlayerAction
    all_video_cards = models.VideoCard.objects.all()
    all_cpus = models.Processor.objects.all()
    all_rams = models.RAM.objects.all()
    all_hdds = models.HDD.objects.all()
    all_ssds = models.SSD.objects.all()
    all_mother_boards = models.MotherBoard.objects.all()
    all_coolings = models.Cooling.objects.all()
    all_power_supplys = models.PowerSupply.objects.all()
    return render(request, 'component_parts/workspace/workspace.html',
                  {'case': case, 'all_video_cards': all_video_cards, 'all_cpus': all_cpus,
                   'all_rams': all_rams,
                   'all_hdds': all_hdds, 'all_ssds':all_ssds,
                   'all_mother_boards': all_mother_boards, 'all_coolings': all_coolings,
                   'all_power_supplys': all_power_supplys, 'model_player_action': model_player_action})


def case_result(request):
    solution = models.PlayerAction.objects.filter(user_id=request.user.id).order_by('-id')[0]
    res = functions_1.general_check_details(solution)
    # solution.delete()
    return render(request, 'component_parts/case_result/case_result.html', {'res': res})


def case_form(request):
    case = models.Case.objects.get(id=randint(1, models.Case.objects.latest('id').id))
    #case = models.Case.objects.filter(case_level=1).get(id=randint(1, models.Case.objects.filter(case_level=1).latest('id').id))
    catalogue = dict(video_card=models.VideoCard.objects.all(), cpu=models.Processor.objects.all(),
                     ram=models.RAM.objects.all(), hdd=models.HDD.objects.all(), ssd=models.SSD.objects.all(),
                     mother_board=models.MotherBoard.objects.all(), cooling=models.Cooling.objects.all(),
                     power_supply=models.PowerSupply.objects.all())
    if request.method == 'POST':
        form = CaseForm(request.POST)
        form.save()
        return redirect('case_result')
    else:
        form = CaseForm({'video_card': get_id(case.video_card), 'cpu': get_id(case.cpu), 'ram': get_id(case.ram), 'hdd': get_id(case.hdd),
                         'ssd': get_id(case.ssd), 'mother_board': get_id(case.mother_board), 'cooling': get_id(case.cooling),
                         'power_supply': get_id(case.power_supply),
                         'case_level': case.case_level, 'budget': case.budget,'user_id': request.user.id})
        return render(request, 'component_parts/case_form/case_form.html', {'form': form, 'case': case, 'catalogue': catalogue})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'component_parts/register/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'component_parts/login.html', {'form': form})


def get_id(obj):
    if obj is None:
        ps = None
    else:
        ps = obj.id
    return ps
