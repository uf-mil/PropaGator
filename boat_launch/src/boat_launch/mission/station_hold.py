#! /usr/bin/env python

import roslib
import rospy
import actionlib
from uf_common.msg import *
from geometry_msgs.msg import Pose, Twist, Vector3, Point, Quaternion
from actionlib_msgs.msg import GoalID
from nav_msgs.msg import Odometry
from std_msgs.msg import Header, Float64


def done():
    rospy.loginfo("New Position Accepted")
    os._exit(0)

def odom_callback(current):
    print 'Waiting for server...'
    client = actionlib.SimpleActionClient('moveto', MoveToAction)
    client.wait_for_server()
    to_send = MoveToActionGoal(
            header = Header(
                stamp=rospy.Time.now(),
                frame_id="/base_link",
            ),
            goal_id = GoalID(
                    stamp=rospy.Time.now(),
                    id = "/goal"
            ),
            goal = MoveToGoal(
                header = Header(
                    stamp=rospy.Time.now(),
                    frame_id="/base_link",
                ),
                posetwist = PoseTwist(
                    pose = Pose(
                        position = Point(x = current.pose.pose.position.x,
                                         y = current.pose.pose.position.y,
                                         z = current.pose.pose.position.z),

                        orientation = Quaternion(x = current.pose.pose.orientation.x,
                                                 y = current.pose.pose.orientation.y,
                                                 z = current.pose.pose.orientation.z, 
                                                 w = current.pose.pose.orientation.w)
                    ),
                    twist = Twist(
                        linear = Vector3(x = current.twist.twist.linear.x,
                                         y = current.twist.twist.linear.y,
                                         z = current.twist.twist.linear.z),
                    
                        angular = Vector3(x = current.twist.twist.angular.x,
                                          y = current.twist.twist.angular.y,
                                          z = current.twist.twist.angular.z)
                    ),
                    acceleration = Acceleration(
                        linear = Vector3(x=0,y=0,z=0),
                        angular = Vector3(x=0,y=0,z=0)
                    )
                ),
                speed = 0,
                uncoordinated = False,
                linear_tolerance = 0,
                angular_tolerance = 0
            )
        )
                
    client.send_goal(to_send, done_cb = done)


rospy.init_node('azi_waypoint_reset')
rospy.Subscriber('/odom', Odometry, odom_callback)
rospy.spin()


            