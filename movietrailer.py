"""Define the Movie class that contains the details of a movie"""
import webbrowser


class Movie():
    VALID_RATING = ["G", "PG", "PG-13", "R"]
    """This class provides a way to store movie related information
    Attributes:
        title: The title of the movie
        storyline: A short description of what the movie is about
        poster_image_url: The URL address of a poster of the movie
        trailer_youtube_url: A link to a YouTube.com trailer"""

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        """Initialises Movie class instance variables"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Plays the movie trailer in the web browser"""
        webbrowser.open(self.trailer_youtube_url)
