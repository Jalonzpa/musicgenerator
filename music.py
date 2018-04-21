import pyaudio
import numpy as np
from random import randint
from random import uniform
p = pyaudio.PyAudio()

print("How many notes do you want there to be in the entire piece?")
choice = int(input())

fs = 100000

for i in range(choice):
	volume = uniform(0.1,1.0)
	duration = uniform(0.25,2.0)
	f = randint(100,2000)
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
