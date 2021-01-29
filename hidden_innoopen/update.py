#!/usr/bin/env python
from itertools import permutations
from random import choice, randint
import qrcode

fn = '/home/clover/catkin_ws/src/clover/clover_simulation/resources/worlds/clover.world'
qr_fn = '/home/clover/.gazebo/models/aruco_map_txt/materials/textures/aruco_marker_2_90.png'
face_fn = '/home/clover/.gazebo/models/{0}/{0}.sdf'

rnd_permutation = lambda x: choice(list(permutations(x,3)))
pose = lambda x_mix, x_max, y_min, y_max: '      <pose>{} {} 0 0 0 0</pose>\n'.format(randint(x_mix, x_max) / 10.0, randint(y_min, y_max) / 10.0)


# QR
qrs = ['yellow','blue','red']
qrcode.make(','.join(rnd_permutation(qrs))).save(qr_fn)


# Photos
names = ["              <name>faces/sherlock</name>\n",
"              <name>faces/jack</name>\n",
"              <name>faces/einstein</name>\n",
"              <name>faces/silverhand</name>\n"]
name = rnd_permutation(names)

for i, dp in enumerate(('dronepoint_blue', 'dronepoint_red', 'dronepoint_yellow')):
    with open(face_fn.format(dp), 'r') as file:
        data = file.readlines()
    
    data[32] = name[i]

    with open(face_fn.format(dp), 'w') as file:
        file.writelines( data )


# Dronepoints
dps = ["      <uri>model://dronepoint_blue</uri>\n",
"      <uri>model://dronepoint_red</uri>\n",
"      <uri>model://dronepoint_yellow</uri>\n"]
dp = rnd_permutation(dps)

# 0.2-2.6, 5.4-8.6
# 5.2-7.6, 5.4-8.6
# 5.2-7.6, 0.4-3.6

with open(fn, 'r') as file:
    data = file.readlines()

data[19], data[24], data[29] = dp
data[21], data[26], data[31] = pose(2,26,54,86), pose(52,76,54,86), pose(52,76,4,36)

with open(fn, 'w') as file:
    file.writelines( data )

print("Updated. Press any key to exit...")
input()
