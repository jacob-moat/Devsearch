from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginationProjects

# Create your views here.


def projects(request):

    projects, search_query = searchProjects(request)
    custom_range, projects = paginationProjects(request, projects, 6)

    context = {'projects': projects, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


def Project(request, pk):
    projectObj = project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, 'Review successfully submited')
        return redirect('Project', pk=projectObj.id)

    context = {'project': projectObj, 'form': form}
    return render(request, 'projects/project.html', context)


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', ' ').split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')
    context = {'form': form, 'project': project}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    Project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        Project.delete()
        return redirect('account')
    context = {'object': Project}
    return render(request, 'delete_template.html', context)