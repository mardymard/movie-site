import media
import fresh_tomatoes

#Each movie is instanstiated using the Movie class located in the media module.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

friday = media.Movie("Friday",
                        "A story of a coupled of friends spending their Friday with no work",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/2/27/Fridayposter1995.jpg/215px-Fridayposter1995.jpg",
                        "https://www.youtube.com/watch?v=umvFBoLOOgo")

back_to_the_future = media.Movie("Back to the Future",
                        "Marty is forced to time travel 30 years into the past to escape a conflict.  He now needs to find a way back home.",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Back_to_the_Future.jpg/220px-Back_to_the_Future.jpg",
                        "https://www.youtube.com/watch?v=qvsgGtivCgs")

addams_family = media.Movie("Addams Family",
                        "The greatest creepy family ever.",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/0/04/The_Addams_Family.jpg/220px-The_Addams_Family.jpg",
                        "https://www.youtube.com/watch?v=LyyJYyIexq8")

jurassic_park = media.Movie("Jurassic Park",
                        "Dinosaurs everywhere",
                        "http://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                        "https://www.youtube.com/watch?v=lc0UehYemQA")

#Create a list for the open_movies_page method in the fresh_tomatoes module. 
movies = [toy_story, avatar, friday, back_to_the_future, addams_family, jurassic_park]

#Launch the movies website
fresh_tomatoes.open_movies_page(movies)


