from django.shortcuts import render, reverse, HttpResponseRedirect
from recipebox.models import Recipes, Author, User
from recipebox.forms import RecipesForm, AuthorsForm, LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib.auth.models import User


def hello(request):
    html = 'hello.html'
    items = Recipes.objects.all().order_by('title')
    return render(request, html, {'list': items})


def details(request):
    html = 'recipes.html'
    items = Recipes.objects.all().filter(id=id)
    instructions = items[0].instructions.split('\n')
    return render(request, html, {'recipes': items, 'instructions': instructions})


def recipe_info(request, id):
    html = 'recipe_info.html'
    items = Recipes.objects.all().filter(id=id)
    instructions = items[0].instructions.split("\n")
    return render(request, html,
                  {"recipes": items, "instructions": instructions})


@login_required()
def add_recipe(request):
    html = 'add_recipe.html'
    form = None
    if request.method == "POST":
        form = RecipesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipes.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time_req=data["time_req"],
                instructions=data["instructions"],
            )
        return render(request, "added.html")
    else:
        form = RecipesForm()
    return render(request, html, {"form": form})


def author_info(request, id):
    html = 'author_info.html'
    authors = Author.objects.all().filter(id=id)
    items = Recipes.objects.all().filter(author_id=id)
    return render(request, html, {"authors": authors, "recipes": items})


@login_required()
@staff_member_required()
def add_author(request):
    html = 'add_author.html'
    form = None
    if request.method == "POST":
        form = AuthorsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
            )
        return render(request, "added.html")
    else:
        form = AuthorsForm()
    return render(request, html, {"form": form})


def signup(request):
    html = 'signup.html'
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data["username"], data["email"], data["password"])
            login(request, user)
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
                user=user
            )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})


def login_view(request):
    html = 'login.html'
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


# def logout_view(request):
#     logout(request)
#     html = "hello.html"
#     return render(request, html)
