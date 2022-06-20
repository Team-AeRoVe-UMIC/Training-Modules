# Welcome to Localisation
Congratulations on making it here. Now begins the official part of your subsystem training

* You should be able to view different branches on this repo - you guessed right; these are your subsystem modules
* To clone this repo enter (ssh key should be setup)
 ```sh
git clone git@github.com:Team-AeRoVe-UMIC/Training-Modules.git
```
* Otherwise use
 ```sh
git clone https://github.com/Team-AeRoVe-UMIC/Training-Modules
```
 
* To checkout to another branch
```sh
git checkout <branch_name>
```

# Regarding compute_f_pos.m and compute_focal_length.m

* Dolly Zoom

A dolly zoom is an in-camera effect where you dolly towards or away from a subject while zooming in the opposite direction.
In the given assignment, we are provided with the 3D coordinates, and we have to complete a function, compute focal length that finds focal length such that the height of the object A remains constant while the camera moves along with Z axis. The reference depth, reference focal length and height of the object A and the camera movement will be given

# Regarding est_homography.m and warp_pts.m

* Image Projection

An image projection occurs whenever a flat image is mapped onto a curved surface, or vice versa, and is particularly common in panoramic photography.
The assignment is about projecting the logo of the Penn university onto the goalpoat during a football match.
It involves 2 tasks:
* computing the homography between Penn logo and goal
*  warp the goal points onto the ones in the Penn logo to generate a projection of the logo onto the video frame
