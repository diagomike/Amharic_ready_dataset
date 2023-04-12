import os

def excec(source_dir = 'RTVC_ready',start_batch = 21,batch_size = 3):
    # source_dir = 'RTVC_ready'
    # start_batch = 21
    # batch_size = 3
    for filename in os.listdir(source_dir):
        if filename.endswith('.wav'):
            speaker, utterance_str = filename.split('_d5')
            utterance = int(utterance_str[3:5])
            batch = (utterance - start_batch) // 6 + 1
            new_batch = batch_size * int(speaker) + start_batch - batch + 1
            new_filename = f"{speaker}-{new_batch:02}-{utterance:03}.wav"
            os.rename(os.path.join(source_dir, filename), os.path.join(source_dir, new_filename))
