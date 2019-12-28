from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from geoapp.models import Tree

# Create your views here.
def index(request):
    trees = Tree.objects.all()

    # response = ''

    # for tree in trees:
    #     response = response + "id: {0}, position: {1}".format(str(tree.tree_id), str(tree.position.coords))

    response = serialize('geojson', trees, geometry_field='position', fields=('tree_id',))

    return HttpResponse(response)
