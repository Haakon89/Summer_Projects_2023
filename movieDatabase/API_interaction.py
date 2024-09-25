import requests
from PIL import Image
import io

class APIHandler:
    def __init__(self):
        self.api_key = '299b4a751a3735b38fe785cdd6e68ca9'
        self.base_url = 'https://api.themoviedb.org/3'

    def fetch_movie_data_from_api(self, movie_title):
        search_endpoint = f'/search/movie?api_key={self.api_key}&query={movie_title}'
        search_response = self._send_api_request(search_endpoint)

        if search_response:
            movies = search_response['results']
            if movies:
                movie = movies[0]
                self._fetch_detailed_movie_info(movie)
                self._fetch_movie_credits(movie)
                self._fetch_alternative_titles(movie)
                self._add_poster_url(movie)
                return movie
        return None

    def download_image(self, image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            # Resize the image to half its size
            width, height = image.size
            image = image.resize((width // 2, height // 2), Image.ANTIALIAS)
            return image
        return None

    def _send_api_request(self, endpoint):
        response = requests.get(self.base_url + endpoint)
        if response.status_code == 200:
            return response.json()
        return None

    def _fetch_detailed_movie_info(self, movie):
        details_endpoint = f'/movie/{movie["id"]}?api_key={self.api_key}'
        details_data = self._send_api_request(details_endpoint)
        if details_data:
            # Add additional details to movie dictionary
            movie['production_country'] = details_data.get('production_countries', [{}])[0].get('name', 'N/A')

    def _fetch_movie_credits(self, movie):
        credits_endpoint = f'/movie/{movie["id"]}/credits?api_key={self.api_key}'
        credits_data = self._send_api_request(credits_endpoint)
        if credits_data:
            director = next((crew['name'] for crew in credits_data.get('crew', []) if crew['job'] == 'Director'), 'N/A')
            movie['director'] = director

    def _fetch_alternative_titles(self, movie):
        alt_titles_endpoint = f'/movie/{movie["id"]}/alternative_titles?api_key={self.api_key}&country=NO'
        alt_titles_data = self._send_api_request(alt_titles_endpoint)
        if alt_titles_data:
            norwegian_title = next((title['title'] for title in alt_titles_data.get('titles', []) if title['iso_3166_1'] == 'NO'), 'N/A')
            movie['norwegian_title'] = norwegian_title

    def _add_poster_url(self, movie):
        poster_path = movie.get('poster_path', '')
        movie['poster_url'] = f'https://image.tmdb.org/t/p/w500{poster_path}' if poster_path else 'N/A'
