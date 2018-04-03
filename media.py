import webbrowser

class Movie():
    '''Movie information

        Assigns movie information and opens youtube to show trailer

        Attributes:
            title: string of movie title
            storyline: string summing up the plot of the movie
            poster_image: string url of poster art
            trailer_youtube: string url of youtube trailer

        Methods:
            show_trailer: opens broswer with youtube trailer url
    '''
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''inits Movie class with title, storyline, poster_image, trailer_youtube'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''opens browser with youtube trailer'''
        webbrowser.open(self.trailer_youtube_url)
