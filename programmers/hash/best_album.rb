
genres = ["classic", "pop","classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
songs  = {}
genres.each_with_index do |song_genre, i|
  songs[i] = {genre: song_genre, play: plays[i]}
end

p songs

