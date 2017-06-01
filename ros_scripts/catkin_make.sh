#!/bin/bash
current_dir=`pwd`;
cd ~/ros_ws
if [ $# -ne 1 ];
then
	catkin_make;
else
	catkin_make --pkg $1;
fi
cd $current_dir
exit;
