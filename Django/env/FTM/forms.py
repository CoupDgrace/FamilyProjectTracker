from django import forms

from .models import Members,Tasks,taskNotes

class TasksForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ('taskTitle','assignedMember','taskParent','taskDeadline','taskPriority','taskStatus',)


class  MembersForm(forms.ModelForm):
    
    class Meta:
        model = Members
        fields = ('memberName','memberSquad',)


class TaskNotesForm(forms.ModelForm):
    class Meta:
        model = taskNotes
        fields = ('noteContent',)

