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



def article_detail(request, id):
    """Affiche un article selon son ID"""
    html = f""" 
    <hl>Article #{id} </h1> 
    <p>Vous lisez l'article numéro {id}</p> 
    <a href="/"> <- Retour accueil</a>
    """
    return HttpResponse(html)
    
def user_profile(request, username):
    """Affiche le profil d'un utilisateur""" 
    html = f"""
    <h1>Profil de {username}</h1>
    <p>Bienvenue sur votre profil, {username} !</p>
    <a href="/"> <- Retour accueil</a>
    """
    return HttpResponse(html)
    
def category_products(request, category):
    """Affiche les produits d'une catégorie""" 
    products= {
        'electronique' : ['Laptop', 'Smartphone', 'Tablette'], 
        'vetements' : ['T-shirt', 'Jean', 'Chaussures'], 
        'livres' : ['Python pour débutants', 'Django par la pratique'],
    }

    items = products.get(category, [])
    if items:
        items_html = '<ul>' + ''.join([f'<li>{item}</li>' for item in items]) +'</ul>'
    else:
        items_html = '<p>Catégorie inconnues </p>'
        
    html = f"""
    <h1> Catégorie : {category}</h1>
    {items_html}
    <a href="/"> <- Retour accueil</a>
    """

    return HttpResponse(html)

        