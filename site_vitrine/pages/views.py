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

#----------------Définition des blogs------------------------------------------------------------


# Données simulées (pas encore de base de données)
ARTICLES ={
    1: {
        'title': 'Introduction à Django', 
        'content': 'Django est un framework web Python puissant...', 
        'author': 'Marie',
        'date': '2026-01-01'
    },
    2: {
        'title': 'Les Views en Django', 
        'content': 'Les views gèrent la logique métier...', 
        'author': 'Paul',
        'date': '2026-01-05'
    
    },
    3: {
        'title': 'URLs Dynamiques',
        'content': 'Les paramètres dans les URLs permettent...',
        'author': 'Sophie',   
        'date': '2026-01-06' 
    },
}
        
        
def blog_author(request, author_name):
    """Affiche les articles d'un auteur"""

    author_articles = {
        id: art for id, art in ARTICLES.items()
        if art['author'] == author_name
    }

    if author_articles:
        articles_html = ''
        for id, article in author_articles.items():
            articles_html += f"""
            <li><a href="/blog/article/{id}/">{article['title']}</a></li>
            """

        html = f"""
        <h1>Articles de {author_name}</h1>
        <ul>{articles_html}</ul>
        <a href="/blog/">← Retour au blog</a>
        """
    else:
        html = f"""
        <h1>Aucun article trouvé</h1>
        <p>L'auteur "{author_name}" n'a pas encore d'articles.</p>
        <a href="/blog/">← Retour au blog</a>
        """

    return HttpResponse(html)

def blog_home(request):
    """Liste tous les articles"""
    articles_html= ''
    for id, article in ARTICLES.items():
        articles_html += f"""
        <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
        <h2><a href="/blog/article/{id}/">{article['title']}</a></h2>
        <p><small>Par {article['author']} le {article['date']}</small></p> 
        </div>
        
        """
    html = f"""
    <h1> Mon Blog Django</h1>
    <a href="/"> <- Retour accueil</a> 
    {articles_html}
    """
    return HttpResponse(html)

def blog_article(request, article_id):
    """Affiche un article complet"""
    article = ARTICLES.get(article_id)
    if article:
        html= f"""
        <h1>{article['title']}</h1>
        <p><small>Par {article['author']} le {article['date']}</small></p> 
        <hr>
        <p>{article['content']}</p>
        <hr>
        <a href="/blog/"> <- Retour au blog</a>
        """
    else:
        html = f"""
        <h1>Article non trouvé</h1>
        <p>L'article #{article_id} n'existe pas.</p> 
        <a href="/blog/"> <- Retour au blog</a>
        """
    return HttpResponse(html)

# ---------------------------------------------------

def search(request):
    """Page de recherche avec paramètres GET"""
    query = request.GET.get('q', '') # Récupère le paramètre 'q' 
    category = request.GET.get('category', 'all')
    
    html = f"""
    <h1> Recherche</h1>
    <form method="GET">
        <input type="text" name="q" value="{query}" placeholder="Rechercher...">
        <select name="category">
            <option value="all">Toutes catégories</option> 
            <option value="articles">Articles</option> 
            <option value="produits">Produits</option>
        </select>
        <button type="submit">Rechercher</button>
    </form>
    <hr>
    """
    if query:
        html += f"""
        <h2>Résultats pour "{query}" dans "{category}"</h2> 
        <p>Vous avez recherché : <strong>{query}</strong></p>
        """
    else:
        html += "<p>Entrez un terme de recherche...</p>"
    return HttpResponse(html)



#-----------------------------------------------------------------

def calculatrice(request):
    """Calculatrice Simple""" 
    result = None 
    error = None
    if request.method == 'GET' and 'a' in request.GET:
        try:
            a = float (request.GET.get('a', 0))
            b = float (request.GET.get('b', 0)) 
            operation = request.GET.get('op', 'add')
            if operation == 'add':
                result = a+b 
            elif operation == 'sub': 
                result = a-b 
            elif operation == 'mul':
                result = a*b 
            elif operation == 'div': 
                if b != 0: 
                    result = a/b 
                else:
                    error = "Division par zéro impossible" 
        except ValueError:
            error = "Veuillez entrer des nombres valides"
    
    html= f"""
    <h1> Calculatrice Django</h1>
    <form method="GET">
        <input type="number" step="any" name="a" placeholder="Nombre 1" required>
        <select name="op">
            <option value="add">+</option> 
            <option value="sub">-</option> 
            <option value="mul">x</option> 
            <option value="div">/</option>
        </select>
        <input type="number" step="any" name="b" placeholder="Nombre 2" required> 
        <hr>
        <button type="submit">Calculer</button>
        <hr>
    </form>
    """
    if error:
        html += f"<p style='color: red;'> ❌ {error}</p>"
    elif result is not None:
        html += f"<h2>Résultat {result}</h2>"
    
    html += "<br><a href='/'> <- Retour accueil</a>"
    
    return HttpResponse(html)