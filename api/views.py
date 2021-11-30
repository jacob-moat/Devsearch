from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from projects.views import projects
from .serializers import ProjectSerializer
from projects.models import project, Review, Tag


@api_view(['GET'])
def GetRoutes(request):

    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},

    ]

    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    Project = project.objects.get(id=pk)
    serializer = ProjectSerializer(Project, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
   Project = project.objects.get(id=pk)
   user = request.user.profile
   data = request.data

   review, created = Review.objects.get_or_create(
      owner = user,
      Project = Project,
   )

   review.value = data['value']
   review.save()
   Project.getVoteCount

   serializer = ProjectSerializer(Project, many=False)

   return Response(serializer.data)


@api_view(['DELETE'])
def removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    Project = project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    Project.tags.remove(tag)
    return Response('Tag was removed.')
