import rospy
from sensor_msgs.msg import Image

def Upload_to_Transmitter(data):
    pass

def Upload_callback(data):
    Upload_to_Transmitter(data)


if __name__ == '__main__':

    rospy.init_node('topic_to_transmitter')
    rospy.loginfo("Node topic_to_transmitter started")

    sub = rospy.Subscriber('Cam1_feed', Image, callback = Upload_callback)
    rospy.spin()