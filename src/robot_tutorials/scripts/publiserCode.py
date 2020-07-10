import rospy 
from std_msgs.msg import String  #this code will publishing mesage with String Type

def catkin_talker():
	hello_pub= rospy.Publisher ('hello',String, queue_size=10) #declear the node that publishing hello topic queu_size to limit the number of queued mesages 
	rospy.init_node('catkinE', anonymous=False) # define the name of node , anonymous to ensure thers is no name as the nod name
	rate=rospy.Rate(10) # the node will publish 10 times/sec
	while not rospy.is_shutdown(): #chick if ctrl+c is pressed if it it true it will exit from the loop
		greeting="Hello, World" #the prodcast
		rospy.loginfo(greeting) # looks for debugging
		hello_pub.publish(greeting) # takes care about publishing prodcasting
		rate.sleep() #sleep if there is no publishing 
if __name__=='__main__':
	try:
		catkin_talker()
	except rospy.ROSLnterruptExcption:  #when press ctrl+c will interrupt ros node exicution 
		pass
		

