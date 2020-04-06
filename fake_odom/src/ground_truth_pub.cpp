/*
 * Copyright 2020 PAL Robotics SL. All Rights Reserved
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited,
 * unless it was supplied under the terms of a license agreement or
 * nondisclosure agreement with PAL Robotics SL. In this case it may not be
 * copied or disclosed except in accordance with the terms of that agreement.
 */

#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>

class OdomTf{

public:
    OdomTf();
    void getInfo(const nav_msgs::Odometry::ConstPtr& msg);
    ros::Time current_time;
    void publishOdom();
    nav_msgs::Odometry odom;
    tf::TransformBroadcaster odom_broadcaster;   
private:  
    ros::NodeHandle nh_;
    ros::Subscriber data_sub_;
    ros::Publisher data_pub_;
  
};

OdomTf::OdomTf(){
    data_sub_ = nh_.subscribe("/ground_truth_odom", 1, &OdomTf::getInfo, this, ros::TransportHints().tcpNoDelay(true));
    data_pub_ = nh_.advertise<nav_msgs::Odometry>("/my_odom", 10);
}
void OdomTf::getInfo(const nav_msgs::Odometry::ConstPtr& msg)
{   
  
    geometry_msgs::TransformStamped odom_trans;

    current_time = ros::Time::now();

    odom_trans.header.stamp = current_time;
    odom_trans.header.frame_id = "odom";
    odom_trans.child_frame_id = "base_footprint";
    odom_trans.transform.translation.x = msg->pose.pose.position.x;
    odom_trans.transform.translation.y = msg->pose.pose.position.y;
    odom_trans.transform.translation.z = msg->pose.pose.position.z;

    odom_trans.transform.rotation.x = msg->pose.pose.orientation.x;
    odom_trans.transform.rotation.y = msg->pose.pose.orientation.y;
    odom_trans.transform.rotation.z = msg->pose.pose.orientation.z;
    odom_trans.transform.rotation.w = msg->pose.pose.orientation.w;

    odom_broadcaster.sendTransform(odom_trans);

    //next, we'll publish the odometry message over ROS
    odom.header.stamp = current_time;
    odom.header.frame_id = "odom";
    odom.child_frame_id = "base_footprint";

    //set the position
    odom.pose.pose.position.x = msg->pose.pose.position.x;
    odom.pose.pose.position.y = msg->pose.pose.position.y;
    odom.pose.pose.position.z = msg->pose.pose.position.z;
    odom.pose.pose.orientation.x = msg->pose.pose.orientation.x;
    odom.pose.pose.orientation.y = msg->pose.pose.orientation.y;
    odom.pose.pose.orientation.z = msg->pose.pose.orientation.z;
    odom.pose.pose.orientation.w = msg->pose.pose.orientation.w;

    odom.twist.twist.linear.x = msg->twist.twist.linear.x;
    odom.twist.twist.linear.y = msg->twist.twist.linear.y;
    odom.twist.twist.angular.z = msg->twist.twist.linear.z;
}

void OdomTf::publishOdom()
{
    data_pub_.publish(odom);
}

int main(int argc, char** argv){
    ros::init(argc, argv, "robot_tf_publisher");
    OdomTf odomtf;
    while(ros::ok())
    {
        odomtf.publishOdom();
        ros::spin();
    }
    return 0;
}
