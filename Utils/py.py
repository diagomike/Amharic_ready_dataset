import os
# ! Do Not Use
# Set the path to the directory containing the albums
path = 'Nestables'

# Set the starting number for the batch folders
batch_num = 21

# Loop through each album in the directory
for album in os.listdir(path):
    album_path = os.path.join(path, album)
    if os.path.isdir(album_path):
        # Split the songs into batches of 6
        songs = os.listdir(album_path)
        batches = [songs[i:i + 6] for i in range(0, len(songs), 6)]
        
        # Create a new folder for each batch and move the songs into it
        for batch in batches:
            batch_folder = os.path.join(album_path, str(batch_num))
            os.makedirs(batch_folder)
            for song in batch:
                os.rename(os.path.join(album_path, song), os.path.join(batch_folder, song))
            batch_num += 1
