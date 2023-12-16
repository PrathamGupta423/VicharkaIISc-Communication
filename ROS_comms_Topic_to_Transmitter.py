import rospy
from sensor_msgs.msg import Image
import cv2, imutils, socket
import numpy as np
import time
import base64

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = 'xyz'#  socket.gethostbyname(host_name)
print(host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
print('Listening at:',socket_address)
fps,st,frames_to_count,cnt = (0,0,20,0)


def Upload_to_Transmitter(data):
    msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
    print('GOT connection from ',client_addr)
    WIDTH=400
    frame = data
    frame = imutils.resize(frame,width=WIDTH)
    encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
    message = base64.b64encode(buffer)
    server_socket.sendto(message,client_addr)

def Upload_callback(data):
    Upload_to_Transmitter(data)


if __name__ == '__main__':

    rospy.init_node('topic_to_transmitter')
    rospy.loginfo("Node topic_to_transmitter started")

    sub = rospy.Subscriber('Cam1_feed', Image, callback = Upload_callback)
    rospy.spin()