
def excec(transcript='transcriptions.txt',start_batch=21,batch_size=3,dest_name='new_transcript.txt'):
    # start_batch = 21
    # batch_size = 3
    filenames = open(transcript,'r',encoding='utf8').read()
    new_transcript = filenames
    for file in filenames.splitlines():
        filename = file.split(' ')[0]
        # if filename.endswith('.wav'):

        speaker, utterance = filename.split('_d5')
        utterance = int(utterance.split('.')[0][3:])
        batch = (utterance - 21) // 6 + 1
        new_filename = f"{speaker}-{batch_size*int(speaker)+start_batch-3+batch:02}-{utterance:03}"
        #os.rename(os.path.join(source_dir, filename), os.path.join(source_dir, new_filename))
        new_transcript = new_transcript.replace(filename, new_filename)
    
    open(dest_name,'w',encoding='utf8').write(new_transcript)
