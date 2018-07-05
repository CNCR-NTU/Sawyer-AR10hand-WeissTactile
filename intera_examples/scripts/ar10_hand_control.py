#!/usr/bin/env python

'''
This script starts grabbing motion whilst listening tactile fingertips data.
This is a rather simplistic way of controlling.
Once tactile finger tips reach threshold values for pressure, it receives 'q' message
which when registered will stop the motion. At this point, the subscription is dropped. 
Since, it is an infinite loop it will keep on listening and that may result in further movement of the hand
which is not desireable.

'''

from ros_ar10_class import ar10
import serial
import rospy
hand = ar10()
def movement(target,targetstep,thumbpos_1,thumbpos_2):
	target = target - targetstep
	hand.move(0,thumbpos_1)
	hand.move(1,thumbpos_2)
	hand.move(4,7000)
	hand.move(5,target)
	hand.move(8,7000)
	hand.move(9,target)
	if target <4000:
		target = 4000


        
