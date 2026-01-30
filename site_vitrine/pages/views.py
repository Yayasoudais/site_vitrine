from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    html ="""
    <h1> 🏠 Page d'accueil </h1>
    <nav>
        <a href = "/about/"> À propos </a>
        <a href = "/services/"> Services </a>
        <a href = "/portfolio/"> Portfolio </a>
        <a href = "/contact/"> Contact </a>
    </nav>
    <p> Bienvenue sur mon site professionnel ! </p>
    
    """
    return HttpResponse(html)

def about(request):
    html = """
        <h1>👤 À propos </h1>
        <a href = "/"> <- Retour accueil </a>
        <p>Développeur django pasionnée </p>
    """
    return HttpResponse(html)

def services(request):
    html = """
        <h1>🧰 Nos Services </h1>
        <a href = "/"> <- Retour accueil </a>
        <u>
            <li> Développement web </li>
            <li> APIs Rest </li>
            <li> Consulting Django </li>
        </u>
        """
    return HttpResponse(html)

def portfolio(request):
    html = """
        <h1>🧠 Nos Services </h1>
        <a href = "/"> <- Retour accueil </a>
        <p>Projets réalisés : E-commerce, Blog, CRM </p>
        """
    return HttpResponse(html)

def contact(request):
    html = """
        <h1>💼 Contact </h1>
        <a href = "/"> <- Retour accueil </a>
        <p>Email : dev@monsite.com </p>
        """
    return HttpResponse(html)


        