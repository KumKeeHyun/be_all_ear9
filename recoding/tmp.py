import pyaudio
import wave

form1 = pyaudio.paInt16
chan = 1
samp_rate = 44100
chunk = 1024
record_secs = 3
dev_index = 2
wav_output_filename = 'test1.wav'

audio = pyaudio.PyAudio()

stream = audio.open(format = form1, rate = samp_rate, channels = chan, input_device_index = dev_index, input = True, frames_per_buffer = chunk)
print("recording")
frames = []

for ii in range(0, int(samp_rate / chunk * record_secs)):
	data = stream.read(chunk)
	frames.append(data)

print("finished")

stream.stop_stream()
stream.close()
audio.terminate()

wavefile = wave.open(wav_output_filename, 'wb')
wavefile.setchannels(chan)
wavefile.setsamewidth(audio.get_sample_size(form1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
