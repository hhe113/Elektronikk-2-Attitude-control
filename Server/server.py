import datetime as dt
import socket
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint


# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific IP address and port number (replace BIND_IP and BIND_PORT with your desired values)
s.bind(('10.42.0.1', 9876))

# listen for incoming connections
s.listen(1)

# accept a connection from a client
conn, addr = s.accept()

# print the client's IP address
print('Connected by', addr)

# create a figure and axis object
fig = plt.figure() 
ax = fig.add_subplot(1,1,1)
xs = []
ys = []

def update(i,xs,ys):
    # read the data from IMU
    imu_data_string = str(conn.recv(1024))
    print(imu_data_string)
    imu_data_string = imu_data_string[3:-2]

    imu_data_string = imu_data_string.split(",")

    print(imu_data_string)
    
    imu_data = []
    for x in imu_data_string:
        imu_data.append(float(x))

    print(imu_data)

    accelZ = float(imu_data[2])
    print (accelZ)
    
    # add the new data to the plot
    xs.append(i)
    ys.append(accelZ)

    xs = xs[-50:]
    ys = ys[-50:]

    # clear and drwa the plot again
    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Z acceleration over Time')
    plt.ylabel('Acceleration (m/s^2)')


# create an animation object to continuously update the plot
ani = animation.FuncAnimation(fig, update,fargs=(xs,ys), interval=50, blit=True)

# show the plot
plt.show()