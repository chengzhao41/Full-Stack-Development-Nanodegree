import webbrowser


class Movie():
    """
    This class encompass a movie. Its fields include anything that is directly related to movies.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date):
        """
        This is the constructor.
        :param movie_title:  The title of the movie.
        :param movie_storyline: The story line of the movie.
        :param poster_image: A link to the movie poster image.
        :param trailer_youtube: A link to the youtube trailer.
        :param release_date: The release date of the movie.
        :return: The movie object.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date

    def show_trailer(self):
        """
        Opens the default web broser and goes to the youtube url.
        """
        webbrowser.open(self.trailer_youtube_url)
