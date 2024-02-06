from django.shortcuts import render

def hi(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def registration(request):
    return render(request, 'myapp/registration.html')


# from django.shortcuts import render

# def registration(request):
#     if request.method == 'POST':
        
#         return render(request, 'myapp/registration_success.html')
#     return render(request, 'myapp/registration.html')


