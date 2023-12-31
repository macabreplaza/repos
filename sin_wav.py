reset
#from tutorialspoint
#https://www.tutorialspoint.com/how-to-plot-a-wav-file-using-matplotlib

from scipy.io.wavfile import read
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
input_data = read("16bit4chan.wav")
audio = input_data[1]
plt.plot(audio[0:1024])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()
