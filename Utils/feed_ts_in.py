import os

def excec(source_dir = 'ready',transcription_file = 'new_transcript.txt',destination_dir = 'ready',trans=True):
    # source_dir = 'ready'
    # transcription_file = 'new_transcript.txt'
    # destination_dir = 'ready'
    if trans: trans = 'trans'
    else: trans = 'alignment'

    transcriptions = {}
    for line in open(transcription_file, 'r',encoding='utf8').readlines():
        # Split by space might have been a better option but yeah, it works
        # key= line.split(' ')[0];value line.replace(key,'').strip()
        transcriptions[line[:9]] = line[10:]

    for _, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.wav'):
                speaker, speech_set, _ = file.split('-')
                destination_path = os.path.join(destination_dir, speaker, speech_set)
                transcription = transcriptions[file[:-4]] # remove extention
                with open(os.path.join(destination_path, f'{speaker}-{speech_set}.{trans}.txt'), 'a',encoding='utf8') as f:
                    f.write(file+" "+transcription)