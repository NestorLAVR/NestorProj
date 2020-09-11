from django.shortcuts import render
from . forms import UserForm
from . function import VisualizeData

def index(request):
    submitbutton = request.POST.get("submit")
    agregations = 'sum'
    choose1, choose2, visual,img = '', '', '', ''
    form = UserForm(request.POST)
    if form.is_valid():
        choose1 = form.cleaned_data.get("choose1")
        choose2 = form.cleaned_data.get('choose2')
        visual = form.cleaned_data.get('choose_Visualization') #получение данных из сайта
        if choose1 !=None and visual != None and choose2 != None:
            visual, choose1, choose2 = str(visual),str(choose1), str(choose2)
            if choose1[-8:]=='duration' or choose1[-8:] =='Duration':
                agregations = 'avg'
            if choose1[-13:]=='authenticated':
                agregations = 'unique'
            img = VisualizeData(choose1 ,choose2 ,visual, agregations)



    context = {'form': form,   'data': img,
               'submitbutton': submitbutton }

    return render(request, 'simple/index.html', context)
