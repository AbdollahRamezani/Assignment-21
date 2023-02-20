import pysynth

notes1 = (('c', 4), ('e', 4), ('g', 4), ('c5', 2))
notes2 = (('e5', 2), ('d5', 2), ('c5', 2))
notes3 = (('g4', 2), ('f4', 2), ('e4', 2))
notes4 = (('c4', 4), ('g3', 4))

pysynth.make_wav(notes1, fn="flute_music1.wav")
pysynth.make_wav(notes2, fn="flute_music2.wav")
pysynth.make_wav(notes3, fn="flute_music3.wav")
pysynth.make_wav(notes4, fn="flute_music4.wav")