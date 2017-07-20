import webbrowser

'''This is movie class will instantiate a movie object'''


class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    '''This constructor will initialize the movie object with given inputs'''
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    '''This method will lauch a trailer for the movie that is selected'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
