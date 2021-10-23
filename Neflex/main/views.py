from django.shortcuts import render
from requests import get
from bs4 import BeautifulSoup as Soup

# Create your views here.
def index(request):
    url = get('https://www.imdb.com/title/tt2382320/')
    req = url.text
    soup_data = Soup(req, 'html.parser')
    movies = soup_data.findAll('div', {'class' : 'ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width Poster__CelPoster-sc-6zpm25-0 kPdBKI celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2'})
    movie_id = 2382320
    image = movies[0].div.img['srcset'].split(',')[-4] + ",0,285,422_.jpg"
    context = {
        'image': image,
        'movie_id': movie_id
    }
    
    return render(request, "main/index.html", context=context)


def about(request):
    return render(request, 'main/about.html')


def movie(request, movie_id):
    context = {
        'movie_id': movie_id
    }
    return render(request, 'main/movie.html', context=context)