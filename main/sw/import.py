import wave


class ImportWav(object):
    """ Class for importing wav files """

    
    def __init__(self, wav_file):

        self.wav = wav_file
        
    def print_wav(self):

        raw_wav = wave.open(self.wav, 'r')
        print "Chanels: {}".format(raw_wav.getnchannels())
        print "Sample Width : {}".format(raw_wav.getsampwidth())

if __name__ == "__main__":

    bitch = ImportWav("BITCH.WAV")
    bitch.print_wav()

