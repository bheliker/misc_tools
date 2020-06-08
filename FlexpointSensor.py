#this should be pasted and run inside a Jupyter notebook
import serial, time
import matplotlib.pyplot as plt

%pylab inline

# Open the Serial Port (your address may vary)
s = serial.Serial(port='/dev/tty.usbmodem1451', baudrate=9600)
time.sleep(1)
s.write('enable\r\r')

line = s.readline()
line = s.readline()
line = s.readline()

#record data
data = 0 
dataArray = []

while abs(data) < 2000:
    line = s.readline()
    data = float(line.split('[')[1].split(']')[0])
    dataArray.append(data)
    #print data

# close the Serial port
s.write('disable\r\r')
time.sleep(1)
s.close()

# Plot the data
print len(dataArray)

fig = plt.figure(facecolor = '0.15')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_axis_off()
fig.add_axes(ax)

plt.plot(dataArray, color = 'skyblue', linewidth = 2.5, alpha = 0.79)
fig.set_size_inches(18.5, 5.5)
plt.show()
