#!/usr/bin/env python
import rospy
import ros_numpy
import sensor_msgs.point_cloud2 as pc22
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2 as pc2
from laser_geometry import LaserProjection


class Laser2pc():
	#lst = []
	def __init__(self):
		pass
	def subscriber(self):
		rospy.Subscriber("/laserscan",LaserScan,self.callbac)
		rospy.spin()
		
	def callbac(self,msg):
		lst = []
		self.converter = LaserProjection()
		cloud = self.converter.projectLaser(msg)
		self.pub = rospy.Publisher("/pc",pc2,queue_size = 1)
		self.pub.publish(cloud)
		
		for p in pc22.read_points(cloud,field_names=("x","y","z"),skip_nans = True):
			lst.append((p[0],p[1],p[2]))
		print(lst)		
		print("")
		print("-------------------")
		print("")
if __name__ == "__main__":
	rospy.init_node("laserprojector")	
	obj = Laser2pc()
	obj.subscriber()
	#rospy.spin()
		

