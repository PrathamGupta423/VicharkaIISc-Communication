import rospy
from sensor_msgs.msg import Image

def getImg():
    # Get the image from the camera
    # return the image
    pass

if __name__ == '__main__':
    rospy.init_node('camera_to_topic')
    rospy.loginfo("Node camera_to_topic started")
    pub = rospy.Publisher('Cam1_feed', Image, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        frame = getImg()
        pub.publish(frame)
        rate.sleep()

