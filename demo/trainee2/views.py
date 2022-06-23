from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Trainee,Course
# Create your views here.
def listTrainee(request):
    trainees = Trainee.objects.all()
    return render(request, 'index.html', context={"trainees": trainees})

    #return render(request,'base.html')




def Insert(request):
    if request.POST:
        print(request.POST)
        #courseOBJ = Course.objects.get(id = request.POST["course"])
        #Trainee.objects.create(name = request.POST["name"],branch= request.POST["branch"], course = courseOBJ)
        Trainee.objects.create(name=request.POST['name'], courses=Course.objects.get(id=request.POST["course"]),
                               branch=request.POST['branch'])
        return redirect("/trainee2/listTrainee")



    courses= Course.objects.all()
    return render(request,'insert.html',context={"courses":courses})




def Update(req,id):
    trainees = get_object_or_404(Trainee, pk=id)
    courses = Course.objects.all()

    if (req.method == 'GET'):
           return render(req, 'update.html',context={'trainees':trainees,'courses':courses})
    else:

        Trainee.objects.filter(id=id).update(name=req.POST['name'],
                             courses=Course.objects.get(id=req.POST['course']),
                            branch=req.POST['branch'])

        return redirect("/trainee2/listTrainee")




def Delete(request,id):
    trainees = get_object_or_404(Trainee,pk=id)
    trainees.delete()
    return redirect('/trainee2/listTrainee')


