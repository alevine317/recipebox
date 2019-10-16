"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebox.views import hello, author_info, recipe_info, add_recipe, add_author, login_view, logout_view, signup
from recipebox.models import Recipes, Author

# admin.site.register(Recipes)
# admin.site.register(Author)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello, name='homepage'),
    path("author/<int:id>", author_info),
    path("recipes/<int:id>", recipe_info),
    path("addrecipe/", add_recipe),
    path("addauthor/", add_author),
    path("signup/", signup),
    path("login/", login_view),
    path("logout/", logout_view)
]
