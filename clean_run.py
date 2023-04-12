# py.py // old renamer //Unusable

# ren.py // to remane Audio files to Libri 
# bing_opt.py // bing alternative to remane
# text_ren.py // rename file names in the transcript.txt 
# Lib_nest.py // nests audio files according to name
# feed_ts_in.py // Transcription to sub folder feeder
# tGrd_aln.py // Generate aligment.txt from .TextGrid
from Utils import ren 
from Utils import bing_opt 
from Utils import Lib_nest

from Utils import text_ren 
from Utils import feed_ts_in 

from Utils import tGrd_aln

# ?  Audio Correction
# ren.excec()
# Lib_nest.excec()

# ? Text Transcription Correction
# text_ren.excec() 
feed_ts_in.excec()

# ? Alignment Correction
# tGrd_aln.convert_textgrid_to_alignment()
# text_ren.excec('alignment.txt',dest_name='align.txt')
feed_ts_in.excec(transcription_file='align.txt',trans=False)
