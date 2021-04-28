from django.http import HttpResponse

def loginpage(request):
    file_data = open(r'C:\Users\spoorthy\Desktop\django project1\project4\pro4\login.html','r')
    data1 = file_data.read()
    return HttpResponse(data1)