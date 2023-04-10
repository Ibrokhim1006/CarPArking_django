from django.shortcuts import redirect,render

def get_users(get_res):
    def middleware(request):
        request.get_us = request.user.id
        response = get_res(request)
        
        return response
    return middleware