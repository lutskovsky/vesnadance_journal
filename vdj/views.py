from django.shortcuts import render

from .models import Group, Lesson, LessonForm


def index(request):
    groups = Group.objects.all()
    return render(request, 'vdj/index.html', {'groups': groups})


def group(request, group_id):
    lessons = Lesson.objects.filter(group_id=group_id)
    return render(request, 'vdj/group.html', {'lessons': lessons})

def add_lesson(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LessonForm(request.POST)
        # check whether it's valid:
        '''if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')'''

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LessonForm()

    return render(request, 'vdj/add_lesson.html', {'form': form})
