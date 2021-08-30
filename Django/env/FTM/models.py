from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Members(models.Model):
    '''Members who can be assigned tasks'''
    
    ### Fields ###

    memberName = models.CharField(max_length=15) 
    memberSquad = models.CharField(max_length=15)
    memberIsAssignedTask = models.BooleanField(default=False, blank=True)

    ### Methods ###

    def __str__(self): 
        return self.memberName



class Tasks(models.Model):
    ''' Tasks or Ticket objects '''
    ### Enum Classes ###
    class priorityChoice(models.IntegerChoices):
        LIHU = 2, _('Low Impact - High Urgency')
        LILU = 4, _('Low Impact - Low Urgency')
        HIHU = 1, _('High Impact - High Urgency')
        HILU = 3, _('High Impact - Low Urgency')

    class statusChoice(models.TextChoices):
        backlog = 'Backlog'
        inprogress = 'In Progress'
        blocked = 'Blocked'
        complete = 'Complete'

    ### Fields ###

    taskTitle = models.CharField(max_length=25)
    assignedMember = models.ForeignKey(Members, on_delete=models.PROTECT)
    taskParent = models.IntegerField(null=True, blank=True)
    taskCreatedDateTime = models.DateTimeField(auto_now_add=True)
    taskDeadline = models.DateTimeField(null=True, blank=True)
    taskPriority = models.IntegerField(choices=priorityChoice.choices, default=priorityChoice.LILU)
    taskHasChild = models.BooleanField(default=False,blank=True)
    taskStatus = models.CharField(choices=statusChoice.choices, max_length=20, default=statusChoice.backlog)
    taskPercentComplete = models.SmallIntegerField(default=0,blank=True)

    ### Methods ###

    def __str__(self):
        return self.taskTitle

    

class taskNotes(models.Model):
    '''Many to one notes for the tasks'''

    ### Fields ###

    noteContent = models.CharField(max_length=500)
    taskTitle = models.ForeignKey(Tasks, on_delete=models.PROTECT)
    memberName = models.ForeignKey(Members, on_delete=models.PROTECT)
    noteDateTime = models.DateTimeField(auto_now=True)
    
    ### Methods ###

    def __str__(self):
        return self.noteContent