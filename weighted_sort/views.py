from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import json

from weighted_sort.sort import sort

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
    try:
        result = {"sorted": sort(data["items"], data["weights"])}
    except AttributeError:
        r = HttpResponseBadRequest("400 Bad Request: Wrong JSON data")
        r.write("The following fields must be present: items, weights")
        return r

    return JsonResponse(result)
