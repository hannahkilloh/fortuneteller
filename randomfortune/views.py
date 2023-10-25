from django.shortcuts import render
import random

fortuneList = ["Your luck is about to change", "Aliens...", "You left the oven on"]


# Create your views here.
def fortune(request):
    fortune = random.choice(fortuneList)
    context = {'fortune': fortune}
    return render(request, "fortune.html", context)
