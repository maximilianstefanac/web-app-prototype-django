from django.shortcuts import render
from django.http import HttpResponse
from geoapp.models import Tree

# Create your views here.
def index(request):
    trees = Tree.objects.all()

    response = ''

    for tree in trees:

        tree_string = "id: %s, position: %s".format(str(tree.tree_id), str(tree.position))
        response.join(tree_string)

    return HttpResponse(response)
