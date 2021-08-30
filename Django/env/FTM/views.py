from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q

# Create your views here.
# Home Page
def home(request):
    nTicks = Tasks.objects.filter(assignedMember = 1)
    kTicks = Tasks.objects.filter(assignedMember = 2)
    gTicks = Tasks.objects.filter(assignedMember = 3)
    eTicks = Tasks.objects.filter(assignedMember = 4)
    tTicks = Tasks.objects.filter(assignedMember = 5)
    mTicks = Tasks.objects.filter(assignedMember = 6)
    backTicks = Tasks.objects.filter(Q(taskStatus='backlog') | Q(taskStatus='Backlog'))
    doneTicks = Tasks.objects.filter(Q(taskStatus='Complete') | Q(taskStatus='complete'))
    waitTicks = Tasks.objects.filter(taskStatus='waiting')


    return render (
        request,
        'FTM/HTML/BanksBoardIndex.html',
        {'nTicks': nTicks, 'backTicks':backTicks, 'kTicks':kTicks, 'gTicks':gTicks, 'eTicks':eTicks, 'tTicks':tTicks, 'mTicks':mTicks, 'doneTicks':doneTicks, 'waitTicks':waitTicks},
    )   

'''def admin(request):
    return render (
        request,
        'admin/',
    )'''
# # # A few forms # # #

# Members Form
'''
def Members(request):
    memForm = MembersForm()
    return render(request,'FTM/HTML/membersForm.html',{'form':form})

    '''