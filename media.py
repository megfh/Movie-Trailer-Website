class Movie():
    """
    A class representing a movie
    Attributes:
        Title
        Poster
        Trailer URL
    """

    def __init__(self, movie_title, movie_poster, movie_trailer):
        """
        constructor for class Movie
        Takes in inputs for the movie's title, poster and trailer
        and initializes the respective instance variables with the
        given input
        """
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
