import media
import fresh_tomatoes

"""
This file creates 3 instances of movie class, puts them in an array.
It then calls fresh_tomatoes, which populates the movie website with the movie instances and opens the page.
"""

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xxlg.jpg", # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc", # noqa
                        "Nov 1999"
                        )

the_terminal = media.Movie("The Terminal",
                           "A story of a man trapped in JFK International Airport",
                           "https://upload.wikimedia.org/wikipedia/en/8/86/Movie_poster_the_terminal.jpg", # noqa
                           "https://www.youtube.com/watch?v=ciByvddyHBs", # noqa
                           "Oct 2004"
                           )

spectre = media.Movie("Spectre",
                      "James Bond has a secret from the past",
                      "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg", # noqa
                      "https://www.youtube.com/watch?v=ashLaclKCik", # noqa
                      "Nov 2015"
                      )

movies = [toy_story, the_terminal, spectre]
fresh_tomatoes.open_movies_page(movies)
