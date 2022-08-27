from django.shortcuts import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    content_type = request.contect_type
    cookies = request.cookies

    return HttpResponse(f'''
    <p>Host: {host}</p>
    <p>Path: {path}</p>
    <p>UserAgent: {user_agent}</p>
    <p>{cookies}<p>

    ''')

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contacts")

def people(request, name, age):
    return HttpResponse(f'''
    <h2>User into:</h2>
    <p> {name} </p>
    <p>Age {age}</p>
    ''')
    