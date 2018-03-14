import wave

def sopen(filename):
    f = wave.open(filename, 'w')
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(44100)
    return f

def swrite(f, samp_l, samp_r):
    samp = bytearray(2*2)
    samp_l = int((samp_l + 1.0)/2 * 65535) - 2**15
    samp_r = int((samp_r + 1.0)/2 * 65535) - 2**15
    samp[0] = samp_l & 255
    samp[1] = (samp_l & 255 * 256) / 256
    samp[2] = samp_r & 255
    samp[3] = (samp_r & 255 * 256) / 256
    f.writeframes(buffer(samp))

def swrite_long(f, samp_l, samp_r):
    assert(len(samp_l) == len(samp_r))
    l = len(samp_l)
    samp = bytearray(2*2*l)
    for i in xrange(l):
        sl = int((samp_l[i] + 1.0)/2 * 65535) - 2**15
        sr = int((samp_r[i] + 1.0)/2 * 65535) - 2**15
        samp[i*4 + 0] = sl & 255
        samp[i*4 + 1] = (sl & 255 * 256) / 256
        samp[i*4 + 2] = sr & 255
        samp[i*4 + 3] = (sr & 255 * 256) / 256
    f.writeframes(buffer(samp))

def sclose(f):
    f.close()
