import os
def excec(source_dir='Nestabes',start_batch = 21,batch_size = 3):
    # source_dir = 'Nestabes'
    # start_batch = 21
    # batch_size = 3
    for filename in os.listdir(source_dir):
        if filename.endswith('.wav'):
            speaker, utterance = filename.split('_d5')
            utterance = int(utterance.split('.')[0][3:])
            batch = (utterance - 21) // 6 + 1
            new_filename = f"{speaker}-{batch_size*int(speaker)+start_batch-3+batch:02}-{utterance:03}.wav"
            os.rename(os.path.join(source_dir, filename), os.path.join(source_dir, new_filename))

