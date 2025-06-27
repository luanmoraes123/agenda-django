from django.shortcuts import render


from ..forms import RegisterForm


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()

    context = {
        "form": form,
    }
    return render(request, 'contact/register.html', context)
