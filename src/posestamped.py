
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
import math
from std_msgs.msg import Bool

class publish_carre:
	def __init__(self,distance,x=0,y=0):
		self.pub= rospy.Publisher('La trajectoire du carre',PoseStamped, queue_size=10)
        	rospy.init_node('talker')
        	self.rate = rospy.Rate(15)
		self.trajet = distance
        	self.x = 0
		self.y = 0
		self.go = False

	def run(self):

		msg = PoseStamped()
                msg.header.frame_id = "map"
                msg.pose.position.x = self.x
		msg.pose.position.y = self.y

		sur_x = True
		compteur = 0
		en_avant = True
		i = 0
		while not rospy.is_shutdown():


			if (compteur % 2 == 0 and self.go):
				en_avant = not en_avant	

			while (i < self.distance):
				if rospy.is_shutdown():
						break

				self.listener(Bool,'etat_du_bouton')
				if (not self.go):
					break
				self.mouvement_droit(sur_x,en_avant,1)
				msg.pose.position.x = self.x
				msg.pose.position.y = self.y
				self.pub.publish(msg)
				self.rate.sleep()
				i =+ 1

			else:
				i = 0


			if (not self.go):
				continue		
			sur_x = not sur_x
			compteur += 1


	def mv_droit(self,sur_x, avant, trajet):

		if(avant):		
			if(sur_x):
				self.x -= trajet
			else:
				self.y -= trajet
		else:
			if(sur_x):
				self.x += trajet
			else:
				self.y += trajet

	def callback(self,data):
		self.go = data.data


	def listener(self,type_msg,topic):	
		rospy.Subscriber(topic,type_msg,self.callback)


"""
def talker_func():
	pub= rospy.Publisher('chatter',PoseStamped, queue_size=10)
	rospy.init_node('talker')
	rate = rospy.Rate(15)
	msg = PoseStamped()
	msg.header.frame_id = "map"
	theta = 0
	dt = 0.1
	while not rospy.is_shutdown():
		teta = theta + dt
		my_msg.pose.position.x = math.cos(theta)
		my_msg.pose.position.y = math.sin(theta)
		#print sur le terminal,log,rosout
		rospy.loginfo(msg)
		#publier sur le topic chatter
		pub.publish(msg)
		rate.sleep()
"""
if __name__ == '__main__':
	try:
		talk = publish_carre(5)
		talk.run()
	except rospy.ROSInterruptException:
		pass
