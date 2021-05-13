from django.db import models

# Create your models here.
class Members(models.Model):
    '''Members who can be assigned tasks'''
    
    ### Fields ###

    memberName = models.CharField(max_length=15) 
    memberSquad = models.CharField(max_length=15)
    memberIsAssignedTask = models.BooleanField()



    ### Methods ###

    def __str__(self): 
        return self.memberName



class Tasks(models.Model):
    ''' Tasks or Ticket objects '''

    ### Fields ###

    taskTitle = models.CharField(max_length=25)
    assignedMember = models.ForeignKey(Members, on_delete=models.PROTECT)
    taskParent = models.ForeignKey(Tasks,on_delete=models.PROTECT())
    taskCreatedDateTime = models.DateTimeField(auto_now_add=True)
    taskDeadline = models.DateTimeField()
    taskPriority = models.IntegerField()
    taskHasChild = models.BooleanField()
    taskStatus = models.CharField(max_length=10)
    taskPercentComplete = models.SmallIntegerField()


    ### Methods ###



    def __str__(self):
        return self.taskTitle

    

class taskNotes(models.Model):
    '''Many to one notes for the tasks'''

    ### Fields ###

    noteContent = models.CharField(max_length=500)
    taskTitle = models.ForeignKey(Task, on_delete=models.PROTECT)
    memberName = models.ForeignKey(Members, on_delete=models.PROTECT)
    noteDateTime = models.DateTimeField(auto_now=True)
    
    ### Methods ###

    def __str__(self):
        return self.noteContent