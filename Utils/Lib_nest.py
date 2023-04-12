import os
import shutil

def excec(source_dir = 'Nestabes',destination_dir = 'ready'):
    # source_dir = 'Nestabes'
    # destination_dir = 'ready'

    for filename in os.listdir(source_dir):
        if filename.endswith('.wav'):
            speaker, speech_set, _ = filename.split('-')
            destination_path = os.path.join(destination_dir, speaker, speech_set)
            os.makedirs(destination_path, exist_ok=True)
            shutil.move(os.path.join(source_dir, filename), destination_path)