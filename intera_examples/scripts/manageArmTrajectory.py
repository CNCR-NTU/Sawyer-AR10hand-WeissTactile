'''
@author: Nikesh Lama
Nov 2017
'''

#!usr/bin/python
import os
import rospy
import time
import serial
import subprocess
from std_msgs.msg import String
from ros_ar10_class import ar10


global target,targetstep#these values control the hand movement resolution

################################################################################
#Usage:
# run the server
#	rosrun intera_interface joint_trajectory_action_server.py --mode velocity

#then run this script

#################################################################################


def response(data): # main that is called when a message from commands is recieved
    '''
    Reads in data from tactile sensors.
    either keeps continue grabbing motion or stop based on the readings. 
    '''
    rospy.loginfo(rospy.get_caller_id() + '\nI heard %s', data.data) # logs messages recieved from commands to /rosout
    message = data.data
    global target,targetstep
    if message == "q":
         print("object grabbed!!!!")
         #os.system(r"rosrun intera_examples head_display_image.py -f /home/nikesh/test1.png")
         sub.unregister() #stops listening to the topic
         #hand.move(4,7000)
         #hand.move(5,target+100)
         #hand.move(8,7000)http://021606CP00039.local:11311
         #hand.move(9,target+100)
         print("Finished Grabbing.")
         os.system(r"rosrun intera_examples head_display_image.py -f /home/nikesh/object_grabbed.jpg")
         #print('target value:{}'.format(target+100))
         	
         os.system(r"rosrun intera_examples joint_trajectory_file_playback.py -f cup_grab_2")
         
         os.system(r"rosrun intera_examples head_display_image.py -f /home/nikesh/release.jpg")
         hand.open_hand()
         os.system(r"rosrun intera_examples head_display_image.py -f /home/nikesh/moving_back.jpg")
         os.system(r"rosrun intera_examples joint_trajectory_file_playback.py -f cup_grab_3")
         os.system(r"rosrun intera_examples head_display_image.py -f /home/nikesh/logosaw1.png")
         	
    else:
         print("Complete initial movement")
         #print('target value: {}'.format(target))
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

if __name__ == '__main__':
	#run the first part of the movement
	#display suggestive messages on the screen
	os.system(r"rosrun intera_examples head_display_image.py -f /home/nikesh/objectgrab.jpg")
	#starts moving towards the target
	os.system(r"rosrun intera_examples joint_trajectory_file_playback.py -f cup_grab_1")

        #the second part has to make sure the object is grabbed with information from tactile sensors
        hand = ar10()
	hand.open_hand()
	time.sleep(1)
	
	target = 8000 #initial target is fully stretched
	targetstep = 30
	thumbpos_1 = 6200#servo 0 values got from visual inspection
	thumbpos_2 = 7500#servo 1
	# create hand object
        rospy.init_node('sawyerNode', anonymous=True) # defines anonymous listener node
        rate =rospy.Rate(60)
        sub = rospy.Subscriber('sensorInterrupt', String, response) # Subscribes to publisher node 'commands'
        rospy.spin()


