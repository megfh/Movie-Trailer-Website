import media
import fresh_tomatoes

# create instances for some of my favourite movies
youve_got_mail = media.Movie("You've Got Mail",
  "https://upload.wikimedia.org/wikipedia/en/e/ee/You%27ve_Got_Mail.jpg",
  "https://www.youtube.com/watch?v=jCetfaS7GAo")

good_will_hunting = media.Movie("Good Will Hunting",
  "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",  # N0QA
  "https://www.youtube.com/watch?v=QSMvyuEeIyw")

monster_in_law = media.Movie("Monster in Law",
  "https://upload.wikimedia.org/wikipedia/en/d/d5/Monster-in-Law_poster.JPG",
  "https://www.youtube.com/watch?v=mW4iEGH1-1E")

imitation_game = media.Movie("The Imitation Game",
  "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",  # N0QA
  "https://www.youtube.com/watch?v=S5CjKEFb-sM")

aristocats = media.Movie("The Aristocats",
  "https://upload.wikimedia.org/wikipedia/en/8/8d/Aristoposter.jpg",
  "https://www.youtube.com/watch?v=wjA5LWNUPDY")

quartet = media.Movie("Quartet",
  "https://upload.wikimedia.org/wikipedia/en/1/1d/Quartet-Poster.jpg",
  "https://www.youtube.com/watch?v=wSEnh8Hi62E")

# create a list containing all of the instances created above
movies = [youve_got_mail, good_will_hunting, monster_in_law, imitation_game, aristocats, quartet]

# use the open_movies_page function from fresh_tomatoes to create an HTML file to display the page
fresh_tomatoes.open_movies_page(movies)