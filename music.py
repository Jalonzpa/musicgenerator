import pyaudio
import numpy as np
from random import randint
p = pyaudio.PyAudio()

print("How many notes do you want there to be in the entire piece?")
choice = int(input())

volume = 0.5
fs = 44100
duration = 0.5

for i in range(choice):
	f = randint(250,2000)
	print(f)
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
	stream = p.open(format=pyaudio.paFloat32,
			channels=1,
			rate=fs,
			output=True)

	stream.write(volume*samples)
	stream.stop_stream()
	stream.close()

p.terminate()
