import rosbag
import os
import argparse


parser = argparse.ArgumentParser(description='Split .bag into small slices')
parser.add_argument('-i', help='Input bag file', required=True, type=str, metavar='string')
parser.add_argument('-o', help='Path to store the slices', required=True, type=str, metavar='string')
parser.add_argument('-t', help='Time duration for each slice (in seconds). Default: 30.0s', type=float, default=30.0, metavar='float')
args = parser.parse_args()

filename = os.path.abspath(args.i)
path = os.path.abspath(args.o)
time_period = float(args.t)


print 'Input bag:', filename
print 'Output path: ', path

if not os.path.exists(filename):
    print "Bag file not found"
    exit -1

if not os.path.exists(path):
    os.makedirs(path)

bag = rosbag.Bag(filename)

count = 0
it = bag.read_messages()
last_ts = bag.get_start_time()
index = 1
bag_prefix = path
wbag = rosbag.Bag(os.path.join(bag_prefix, str(index) + '.bag'), 'w')
for msg in it:
    ts = msg.message.header.stamp if hasattr(msg.message, 'header') else msg.timestamp
    ts = ts.to_sec()
    if ts - last_ts > time_period:
        last_ts = ts
        index += 1
        wbag.close()
        wbag = rosbag.Bag(os.path.join(bag_prefix, str(index) + '.bag'), 'w')

    wbag.write(msg.topic, msg.message,
               msg.message.header.stamp if hasattr(msg.message, 'header') else msg.timestamp)

wbag.close()
