# ICP algorithm (Point-to-Point Variant)

The Iterative closest point algorithm is employed to estimate transformation between 2 point clouds such that corresponding points between each set are aligned over each other in space.Initially, we start with a transformation guess which would align the 2 point clouds. Points of set one are transformed into the reference frame of set two.Then each point  in  one  data  set  is  paired  with  the  closest  point  in  the  other data set to form correspondence pairs.To solve for optimal transformation, a point-to-point error metric  is  used in  which the sum  of  the  squared distance  between points  in  each  correspondence  pair  is  minimized.The process is repeated with the transformation we just obtained as our new initial guess. It is iterated until the error becomes smaller than a threshold or it stops changing.

## Closed form solution

The source point cloud and target point cloud are represented as ![equations](https://latex.codecogs.com/svg.latex?\dpi{120}&space;\bg_white&space;\large&space;p_{s}) and ![equations](https://latex.codecogs.com/svg.latex?\dpi{120}&space;\bg_white&space;\large&space;p_{s^{'}}) respectively. For data association between these two sets, brute force search methods has been used. In case when multiple source points are matched with same point from the target set, the pair with minumum distance is retained while others are rejected. Morever, unmatched target points are also removed,which consequently leaves us with best one to one correspondences. Following steps are performed on the resultant point sets to solve for optimal translation and rotation.

- step 1 : Calculate centroids of both point clouds
    
    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5Cmu%20_s%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%20p_%7Bs%7D%5E%7B%28j%29%7D)

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5Cmu%20_%7Bs%27%7D%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%20p_%7Bs%27%7D%5E%7B%28j%29%7D)
    
- step 2 : Compute the spread matrix

    <img src="https://latex.codecogs.com/svg.latex?\large&space;W_{ss^{'}}=\frac{1}{n}\sum_{j=1}^{n}\left&space;(&space;p_{s}^{\left&space;(j&space;\right&space;)}-&space;\mu&space;_{s}\right&space;)\left&space;(&space;p_{s^{'}}^{\left&space;(j&space;\right&space;)}-&space;\mu&space;_{s^{'}}\right&space;)^{T}" title="\large W_{ss^{'}}=\frac{1}{n}\sum_{j=1}^{n}\left ( p_{s}^{\left (j \right )}- \mu _{s}\right )\left ( p_{s^{'}}^{\left (j \right )}- \mu _{s^{'}}\right )^{T}" />

- step 3 : Use SVD to obtain optimal rotation matrix

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20USV%5ET%20%3D%20W_%7Bss%27%7D)

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20C_%7Bs%27s%7D%20%3D%20UV%5ET)
    
    
- step 4 : Obtain translation vector by applying the transform on centroids

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20r%5E%7Bs%27s%7D_%7Bs%7D%20%3D%20%5Cmu%20_s%20-%20C%5E%7BT%7D_%7Bs%27s%7D%5Cmu%20_%7Bs%27%7D)

Repeat until convergence.


# TESTS

The implementation was done in Gazebo simulator(Version 7.0). A hokuyo laser scanner was mounted on top of turtlebot2. Point clouds were recorded in lidar's frame of reference, at two different time instances.The algorithm was used to estimate the transformation between the two different lidar frames of reference, in the global frame of reference.In this way, motion of lidar and conseqeuntly, motion of the turtlebot was evaluated between any two steps of time.





**Test 1 : Translational motion of 1m along positive x-axis**


Source scan:

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/zero_position.png" height="400" width="500"> 

Target scan:

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/translation.png" height="400" width="500">


Resultant Transformation Matrix:

<pre>

M :    [[ 0.99943548  0.03359631  1.01173327]
	
	[-0.03359631  0.99943548  0.03959641]
	
	[ 0.          0.          1.        ]]
</pre>


<img src="https://latex.codecogs.com/svg.latex?\large&space;Translation\:in\:x\:\:\left&space;(&space;t_{x}&space;\right&space;)=1.011\:m" title="\large Translation\:in\:x\:\:\left ( t_{x} \right )=1.011\:m" />

<img src="https://latex.codecogs.com/svg.latex?\large&space;Translation\:in\:y\:\:\left&space;(&space;t_{y}&space;\right&space;)=0.039\:m" title="\large Translation\:in\:y\:\:\left ( t_{y} \right )=0.039\:m" />

<img src="https://latex.codecogs.com/svg.latex?\large&space;Rotation\:\:&space;about\:\:&space;z\:&space;\left&space;(&space;\theta&space;\right&space;)=1.89^{\circ}" title="\large Rotation\:\: about\:\: z\: \left ( \theta \right )=1.89^{\circ}" />


**Iterations :**


<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t1.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t2.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t3.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t4.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t5.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t6.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t7.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_t8.png" height="320" width="400">

**Test 2 : Rotational motion along positive z-axis**

Source scan:

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/zero_position.png" height="400" width="500"> 

Target scan:

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/rotation.png" height="400" width="500"> 

Resultant Transformation Matrix:

<pre>

M :    [[0.97110935 -0.23863495  -0.08952401]
	
	[0.23863495  0.97110935  -0.02823182]
	
	[ 0.          0.          1.        ]]

</pre>

<img src="https://latex.codecogs.com/svg.latex?\large&space;Translation\:in\:x\:\:\left&space;(&space;t_{x}&space;\right&space;)=-0.089\:m" title="\large Translation\:in\:x\:\:\left ( t_{x} \right )=-0.089\:m" />

<img src="https://latex.codecogs.com/svg.latex?\large&space;Translation\:in\:y\:\:\left&space;(&space;t_{y}&space;\right&space;)=-0.028\:m" title="\large Translation\:in\:y\:\:\left ( t_{y} \right )=-0.028\:m" />

<img src="https://latex.codecogs.com/svg.latex?\large&space;Rotation\:\:&space;about\:\:&space;z\:&space;\left&space;(&space;\theta&space;\right&space;)=1.89^{\circ}" title="\large Rotation\:\: about\:\: z\: \left ( \theta \right )=13.8^{\circ}" />

**Iterations :**

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r1.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r2.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r3.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r4.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r5.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r6.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r7.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r8.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r9.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r10.png" height="320" width="400">

<img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r11.png" height="320" width="400"> <img src="https://github.com/harshad1600/ICP/blob/master/src/images/icpplotprime_r12.png" height="320" width="400">

> Blockquote




