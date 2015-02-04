from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import json

def weighted_sort(request):
    if not request.method == "GET":
        return HttpResponseBadRequest("400 Bad Request: Use GET method.")
    if not "json" in request.GET:
        r = HttpResponseBadRequest("400 Bad Request: ")
        r.write("Use json parameter in uri. ")
        r.write("Example: {}".format(request.build_absolute_uri("?json={}")))
        return r
    try:
        data = json.loads(request.GET.get("json", "{}"))
    except ValueError:
        return HttpResponseBadRequest("400 Bad Request: Malformed JSON")
    return HttpResponse("JSON data: {}".format(data))
