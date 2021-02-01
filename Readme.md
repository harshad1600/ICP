# ICP algorithm (Point-to-Point Variant)

The Iterative closest point algorithm is employed to estimate transformation between 2 point clouds such that corresponding points between each set are aligned over each other in space.Initially, we start with a transformation guess which would align the 2 point clouds. Points of set one are transformed into the reference frame of set two.Then each point  in  one  data  set  is  paired  with  the  closest  point  in  the  other data set to form correspondence pairs.To solve for optimal transformation, a point-to-point error metric  is  used in  which the sum  of  the  squared distance  between points  in  each  correspondence  pair  is  minimized.The process is repeated with the transformation we just obtained as our new initial guess. It is iterated until the error becomes smaller than a threshold or it stops changing.

## Closed form solution

The target point cloud and source point cloud are represented as ![equations](https://latex.codecogs.com/svg.latex?\dpi{120}&space;\bg_white&space;\large&space;p_{s}) and ![equations](https://latex.codecogs.com/svg.latex?\dpi{120}&space;\bg_white&space;\large&space;p_{s^{'}}) respectively. For data association between these two sets, brute force search methods has been used. In case when multiple source points are matched with same point from the target set, the pair with minumum distance is retained while others are rejected. Morever, unmatched target points are also removed,which consequently leaves us with best one to one correspondences. Following steps are performed on the resultant point sets to solve for optimal translation and rotation.

- step 1 : Calculate centroids of both point clouds
    
    ![](src/images/img_1.PNG)
    
- step 2 : Compute the spread matrix

    ![](src/images/img_2.PNG)

- step 3 : Use SVD to obtain optimal rotation matrix

    ![](src/images/img_3.PNG)

- step 4 : Obtain translation vector by applying the transform on centroids

    ![](src/images/img_4.PNG)

Repeat until convergence.


# TESTS

The implementation was done in Gazebo simulator(Version 7.0). A hokuyo laser scanner was mounted on top of Turtlebot2. Point clouds were recorded in lidar's frame of reference, at two different time instances.The point cloud recorded first is referred as target set while the current one is referred as source set.The ICP algorithm was used to estimate the transformation between these sets, in the target's frame of reference. In this way, motion of lidar and consequently, motion of the turtlebot was evaluated between two known steps of time.





**Test 1 : Translational motion of 1m along positive x-axis**


[Target scan:](https://github.com/harshad1600/ICP/blob/master/src/data_points/translation)

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/zero_position.png" height="400" width="500"> 

[Source scan:](https://github.com/harshad1600/ICP/blob/master/src/data_points/translation)

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/translation.png" height="400" width="500">


Resultant Transformation Matrix:

<pre>

M :    [[ 0.99943548  0.03359631  1.01173327]
	
	[-0.03359631  0.99943548  0.03959641]
	
	[ 0.          0.          1.        ]]
</pre>


![equation](https://latex.codecogs.com/svg.latex?%5Clarge%20Translation%5C%3Ain%5C%3Ax%5C%3A%5C%3A%5Cleft%28t_%7Bx%7D%20%5Cright%20%29%3D1.011%5C%3Am)

<img src="https://latex.codecogs.com/svg.latex?\large&space;Translation\:in\:y\:\:\left&space;(&space;t_{y}&space;\right&space;)=0.039\:m" title="\large Translation\:in\:y\:\:\left ( t_{y} \right )=0.039\:m" />

<img src="https://latex.codecogs.com/svg.latex?\large&space;Rotation\:\:&space;about\:\:&space;z\:&space;\left&space;(&space;\theta&space;\right&space;)=-1.89^{\circ}" title="\large Rotation\:\: about\:\: z\: \left ( \theta \right )=-1.89^{\circ}" />


**Iterations :**


<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t1.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t2.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t3.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t4.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t5.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t6.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t7.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t8.png" height="320" width="400">

**Test 2 : Rotational motion along positive z-axis**

[Target scan:](https://github.com/harshad1600/ICP/blob/master/src/data_points/rotation)

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/zero_position.png" height="400" width="500"> 

[Source scan:](https://github.com/harshad1600/ICP/blob/master/src/data_points/rotation)

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/rotation.png" height="400" width="500"> 

Resultant Transformation Matrix:

<pre>

M :    [[0.97110935 -0.23863495  -0.08952401]
	
	[0.23863495  0.97110935  -0.02823182]
	
	[ 0.          0.          1.        ]]

</pre>

<img src="https://latex.codecogs.com/svg.latex?\large&space;Translation\:in\:x\:\:\left&space;(&space;t_{x}&space;\right&space;)=-0.089\:m" title="\large Translation\:in\:x\:\:\left ( t_{x} \right )=-0.089\:m" />

<img src="https://latex.codecogs.com/svg.latex?\large&space;Translation\:in\:y\:\:\left&space;(&space;t_{y}&space;\right&space;)=-0.028\:m" title="\large Translation\:in\:y\:\:\left ( t_{y} \right )=-0.028\:m" />

<img src="https://latex.codecogs.com/svg.latex?\large&space;Rotation\:\:&space;about\:\:&space;z\:&space;\left&space;(&space;\theta&space;\right&space;)=13.8^{\circ}" title="\large Rotation\:\: about\:\: z\: \left ( \theta \right )=13.8^{\circ}" />

**Iterations :**

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r1.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r2.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r3.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r4.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r5.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r6.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r7.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r8.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r9.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r10.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r11.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r12.png" height="320" width="400">

> Reference : 

> State estimation and localization for self-driving cars - by University of Torronto (Coursera)




