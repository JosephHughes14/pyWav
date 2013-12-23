import wave


class ImportWav(object):
    """ Class for importing wav files """
    
    def __init__(self, wav_file):

        self.wav = wav_file

    def test_method(self):
        
        return True)
        
    def print_wav(self):

        raw_wav = wave.open(self.wav, 'rb')
        print "Mthods : {}".format(dir(raw_wav))

if __name__ == "__main__":

    bitch = ImportWav("BITCH.WAV")
    bitch.print_wav()

