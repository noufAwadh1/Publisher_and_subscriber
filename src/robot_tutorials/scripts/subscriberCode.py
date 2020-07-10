import rospy 
from std_msgs.msg import String
def callback_str(data):
	rospy.loginfo(data.data) #print the data that receive from rospy.loginfo
def listener():
	rospy.init_node('me', anonymous=False) #subscribe node 
	rospy.Subscriber('hello',String,callback_str) #subscriber node will listen for topic hello
	rospy.spin() 
	
if __name__=='__main__':
	listener()
	
