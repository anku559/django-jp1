from django.shortcuts import render
from django.http import HttpResponse, request

# Request Handler - Request => Response
def test_template(req: request):
    # return HttpResponse("Hello World")
    return render(
        req,
        "hello.html",
        {
            "email": "ankit.zeeweesoft@gmail.com",
            "first_name": "Ankit",
            "last_name": "Singh",
        },
    )


def say_hello(req: request):
    x = 1
    y = 2
    return HttpResponse("Hello World")
