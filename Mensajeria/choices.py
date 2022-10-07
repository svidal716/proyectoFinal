

from requests import request


def obtenerUser(request):
    username = request.user.username
    return username


username = obtenerUser(request)

usuario = [("username", username),

           ]
