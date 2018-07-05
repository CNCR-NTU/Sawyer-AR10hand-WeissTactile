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
import time
import sys
import os
import random
import serial
import subprocess

import rospy
from std_msgs.msg import String 

global target,targetstep#these values control the hand movement resolution

def response(data): # main that is called when a message from commands is recieved
    '''
    Reads in data from tactile sensors.
    either keeps continue grabbing motion or stop based on the readings. 
    '''
    hand = ar10() #creating instance of ar10 hand
    #hand.open_hand() # opens the hand
    rospy.loginfo(rospy.get_caller_id() + '\nI heard %s', data.data) # logs messages recieved from commands to /rosout
    
    message = data.data
    #print(type(option))
    global target,targetstep
    if message == "q":
         print("object grabbed!!!!")
         sub.unregister() #stops listening to the topic
         #hand.move(4,7000)
         #hand.move(5,target+100)
         #hand.move(8,7000)
         #hand.move(9,target+100)
         print("Finished Grabbing.")
         print('target value:{}'.format(target+100))
	 #topicFlag = 0
         #time.sleep(1)
    	
    else:
         print("Carrying on")
         print('target value: {}'.format(target))
         #as it gets carry on message, the hand moves slowly using the target value which will decrease in each iteration
         #slowing contracting the fingers
         # For reference: when the target val is 8000 it means the motors are not engaged resulting in open and extended hand.
         # values decreasing from 8000 to 4200 will constrict the fingers
         target = target - targetstep
         hand.move(0,thumbpos_1)
         hand.move(1,thumbpos_2)
         hand.move(4,7000)
         hand.move(5,target)
         hand.move(8,7000)
         hand.move(9,target)
         if target <4000:
               target = 4000
         
'''		
def movement(obj = ar10()):
	#ring finger        
	obj.move(4,4000)
        obj.move(5,8000)
	#index finger
	obj.move(8,4000)
	obj.move(9,8000)
	obj.wait_for_hand()
'''

if __name__ == "__main__":
	hand = ar10()
	hand.open_hand()
	time.sleep(1)
	hand.close()
	target = 8000 #initial target is fully stretched
	targetstep = 20
	thumbpos_1 = 6300#servo 0 values got from visual inspection
	thumbpos_2 = 7500#servo 1
	# create hand object
    	#initialise the node
	rospy.init_node('listener', anonymous=True) # defines anonymous listener node
	rate =rospy.Rate(10)
	sub = rospy.Subscriber('sensorInterrupt', String, response) # Subscribes to publisher node 'commands'
	rospy.spin()


        
