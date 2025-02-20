import requests
def get_toprated_movies(page=1):
    url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NTljNDhmYzNhYjdkMWJjYzBiNGRhYjhkYmQ0ZmIwZCIsIm5iZiI6MTczMDgzMTU0NS44MzUxNzcyLCJzdWIiOiI2NzFhOGJjMTRiZTE1NDY5ZTcwZDkyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.z8fyjZNdK1Y2azrwchFlW-b-Nh0LapLw7bOjxui3ylM"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print(f"Error get popular movies: {response.status_code}")
        return []
def get_upcoming_movies(page=1):
    url = f"https://api.themoviedb.org/3/movie/upcoming?language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NTljNDhmYzNhYjdkMWJjYzBiNGRhYjhkYmQ0ZmIwZCIsIm5iZiI6MTczMDczOTY5OS40NjY3NTE2LCJzdWIiOiI2NzFhOGJjMTRiZTE1NDY5ZTcwZDkyZGYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.eRjahChQJtPPuB8G-JH_nhNAD3aFp7R9GpzW2ZDdvRM"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print(f"Error get popular movies: {response.status_code}")
        return []
def get_popular_movies(page=1):
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print(f"Error get popular movies: {response.status_code}")
        return []

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error get top rated movies: {response.status_code}")
        return []
def get_movie_images(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error get movie images: {response.status_code}")
        return {} 
def get_similar_movies(movie_id, page=1):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar?language=en-US&page={page}"   
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Error get similar images: {response.status_code}")
        return []
def get_movie_video(movie_id, page=1):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=ua"  
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Error get similar images: {response.status_code}")
        return []
def search_movies(query, page=1):
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsIm5iZiI6MTczMDIyNTQ0MC4yNjk4OTQsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-Z7W_6uoqHPgcn2pSeodC1cPTmpukDXSPBTcwUImVQY"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print(f"Error search movies: {response.status_code}")
        return []