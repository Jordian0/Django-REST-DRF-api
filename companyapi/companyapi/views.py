from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("home page requested")
    names = ['rahul', 'mohan', 'ravi']
    # return HttpResponse("<h1>This is home page<h1>")
    return JsonResponse(names, safe=False)
