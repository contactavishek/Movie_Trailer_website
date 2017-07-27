"""Stores details of movies and displays them on a webpage"""
import fresh_tomatoes
import movietrailer

"""Create instances of the Movie class to hold information of recent \
blockbuster movies with title, storyline, poster image link \
and video trailer link"""


jack_reacher = movietrailer.Movie("Jack Reacher: Never Go Back", "The plot \
                                   follows Reacher going on-the-run \
                                   with an Army Major who has been \
                                   framed for espionage", "https://upload.\
wikimedia.org/wikipedia/en/0/05/Jack_Reacher_Never_Go_Back_poster.jpg", "https:\
//www.youtube.com/watch?v=aRwrdbcAh2s")

accountant = movietrailer.Movie("The Accountant", "Christian Wolff is a math \
                                 savant with more affinity for numbers \
                                 than people. Using a small-town CPA office \
                                 as a cover, he makes his living \
                                 as a freelance accountant for dangerous \
                                 criminal organizations", "https://images-na.\
ssl-images-amazon.com/images/M/MV5BNDc5Mzg2NTYxNV5BMl5BanBnXkFtZTgwM\
jQ2ODAwOTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com\
/watch?v=0KHOVlEpMyY")

sully = movietrailer.Movie("Sully", "The film follows Sullenberger's January \
                            2009 emergency landing of a passenger jet \
                            on the Hudson River", "https://upload.wikimedia.\
org/wikipedia/en/thumb/8/82/Sully_xxlg.jpeg/220px-Sully_xxlg.jpeg", "https:\
//www.youtube.com/watch?v=mjKEXxO2KNE")

dr_strange = movietrailer.Movie("Doctor Strange", "Surgeon Stephen Strange \
                                 learns the mystic arts from the Ancient One \
                                 after a career-ending car accident", "https:\
//upload.wikimedia.org/wikipedia/en/thumb/c/c7/Doctor_Strange_poster.jpg/220px\
-Doctor_Strange_poster.jpg", "https://www.youtube.com/watch?v=HSzx-zryEgM")

inferno = movietrailer.Movie("Inferno", "When Langdon wakes up in an Italian \
                              hospital with amnesia, he teams up with \
                              Sienna Brooks, a doctor he hopes will help \
                              him recover his memories", "https://upload.wiki\
media.org/wikipedia/en/thumb/6/66/Inferno_%282016_film%29.png/220px\
-Inferno_%282016_film%29.png", "https://www.youtube.com/watch?v=RH2BD49sEZI")

arrival = movietrailer.Movie("Arrival", "When multiple mysterious spacecraft \
                              touch down across the globe, an elite team \
                              is put together to investigate", "https://upload.\
wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg", "https://www.you\
tube.com/watch?v=tFMo3UJ4B4g")

allied = movietrailer.Movie("Allied", "In 1942 North Africa, Canadian \
                             intelligence officer Max Vatan meets French \
                             Resistance fighter Marianne Beausejour \
                             on a secret mission behind enemy lines", "https\
://upload.wikimedia.org/wikipedia/en/thumb/4/43/Allied_%28film%29.png/220px\
-Allied_%28film%29.png", "https://www.youtube.com/watch?v=HSCQWX-pUSg")

moana = movietrailer.Movie("Moana", "An adventurous teenager sails out on a \
                            daring mission to save her people", "https://upload\
.wikimedia.org/wikipedia/en/thumb/2/26/Moana_Teaser_Poster.jpg/220px\
-Moana_Teaser_Poster.jpg", "https://www.youtube.com/watch?v=LKFuXETZUsI")

rogue_one = movietrailer.Movie("Rogue One: A Star Wars Story", "In a time of \
                                conflict, a group of unlikely heroes band \
                                together on a mission to steal the plans to \
                                the Death Star", "http://a.dilcdn.com/bl/wp-\
content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg", "https://www.youtube\
.com/watch?v=frdj1zb9sMY")

# Add the movie instances to a list

movies = [jack_reacher,
          accountant,
          sully,
          dr_strange,
          inferno,
          arrival,
          allied,
          moana,
          rogue_one]

# Generate a web page that displays the movies in the list

fresh_tomatoes.open_movies_page(movies)
