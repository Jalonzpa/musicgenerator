import pyaudio
import numpy as np
from random import randint
from random import uniform
p = pyaudio.PyAudio()

print("How many notes do you want there to be in the entire piece?")
choice = int(input())	# stores an int from user in var choice

fs = 100000	# sampling rate in hertz

for i in range(choice):	   # iterates over the int chosen by the user
	volume = uniform(0.1,1.0)	# chooses random float for the volume
	duration = uniform(0.25,2.0)	# chooses random float for the duration
	f = randint(100,2000)	# chooses random int for the frequency
	print(f)
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)	# generates samples and changes it to a float32 array
	stream = p.open(format=pyaudio.paFloat32,
			channels=1,
			rate=fs,
			output=True)

	stream.write(volume*samples)	# plays the sound

	stream.stop_stream()
	stream.close()

p.terminate()
