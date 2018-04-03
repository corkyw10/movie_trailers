import media
import fresh_tomatoes

#Movie class instances
toy_story = media.Movie('Toy Story', 'A story about the shenanigans of toys that come to life when their owner isn\'t around', 'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 'https://youtu.be/4KPTXpQehio')

littlefinger = media.Movie('Littlefinger', 'A story love, loss and hope', 'https://upload.wikimedia.org/wikipedia/en/d/d5/Aidan_Gillen_playing_Petyr_Baelish.jpg', 'https://youtu.be/KwFy_S2f__8')

donnie_darko = media.Movie('Donnie Darko', 'A boy goes on a journey of time travel', 'https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg', 'https://youtu.be/8wqVHjK2bQs')

stranger_than_fiction = media.Movie('Stranger Than Fiction', 'A man finds out his life is being narrated', 'https://upload.wikimedia.org/wikipedia/en/f/ff/Stranger_Than_Fiction_%282006_movie_poster%29.jpg', 'https://youtu.be/PZpg8VII7es')

hairspray = media.Movie('Hairspray', 'A musical about life in 1960\'s Baltimore', 'https://upload.wikimedia.org/wikipedia/en/5/5c/Hairspray2007poster.JPG', 'https://youtu.be/SUoG7mqCixI')

rocky = media.Movie('Rocky', 'A man with a shot at the heavyweight championship', 'https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg', 'https://youtu.be/7RYpJAUMo2M')

#array of movie instances to populate fresh_tomatoes.py
movies = [toy_story, littlefinger, donnie_darko, stranger_than_fiction, hairspray, rocky]

#opens browser with fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)



