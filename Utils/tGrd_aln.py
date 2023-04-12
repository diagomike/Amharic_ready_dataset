import os
from praatio import textgrid

def convert_textgrid_to_alignment(textgrid_dir='align', output_file='aligment.txt'):
   with open(output_file, 'w',encoding='utf8') as f:
      for filename in os.listdir(textgrid_dir):
         tg = textgrid.openTextgrid(os.path.join(textgrid_dir, filename),includeEmptyIntervals=True)
         words = []
         end_times = []
         # Only the word InterValTier
         tier = tg.tiers[0]
         for _, end, label in tier._entries:
            words.append(label)
            end_times.append(str(end))
         f.write(f"{filename.split('.')[0]} \"{','.join(words).upper()}\" \"{','.join(end_times)}\"\n")
    
