# ICP algorithm (Point-to-Point Variant)

The Iterative closest point algorithm is employed to estimate transformation between 2 point clouds such that corresponding points between each set are aligned over each other in space.Initially, we start with a transformation guess which would align the 2 point clouds. Points of set one are transformed into the reference frame of set two.Then each point  in  one  data  set  is  paired  with  the  closest  point  in  the  other data set to form correspondence pairs.To solve for optimal transformation, a point-to-point error metric  is  used in  which the sum  of  the  squared distance  between points  in  each  correspondence  pair  is  minimized.The process is repeated with the transformation we just obtained as our new initial guess. It is iterated until the error becomes smaller than a threshold or it stops changing.

## Closed form solution

The source point cloud and target point cloud are represented as ![equations](https://latex.codecogs.com/svg.latex?\dpi{120}&space;\bg_white&space;\large&space;p_{s}) and ![equations](https://latex.codecogs.com/svg.latex?\dpi{120}&space;\bg_white&space;\large&space;p_{s^{'}}) respectively. For data association between these two sets, brute force search methods has been used. In case when multiple source points are matched with same point from the target set, the pair with minumum distance is retained while others are rejected. Morever, unmatched target points are also removed,which consequently leaves us with best one to one correspondences. Following steps are performed on the resultant point sets to solve for optimal translation and rotation.

- step 1 : Calculate centroids of both point clouds
    
    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5Cmu%20_s%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%20p_%7Bs%7D%5E%7B%28j%29%7D)

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5Cmu%20_%7Bs%27%7D%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%20p_%7Bs%27%7D%5E%7B%28j%29%7D)
    
- step 2 : Compute the spread matrix

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20W_%7Bss%27%7D%20%3D%20%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bj%3D1%7D%5E%7Bn%7D%5Cleft%20%28%20p_%7Bs%7D%5E%7B%28j%29%7D%20-%20%5Cmu%20_s%20%5Cright%20%29%5Cleft%20%28%20p_%7Bs%27%7D%5E%7B%28j%29%7D%20-%20%5Cmu%20_%7Bs%27%7D%20%5Cright%20%29%5E%7BT%7D)
    
- step 3 : Use SVD to obtain optimal rotation matrix

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20USV%5ET%20%3D%20W_%7Bss%27%7D)

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20C_%7Bs%27s%7D%20%3D%20UV%5ET)
    
    
- step 4 : Obtain translation vector by applying the transform on centroids

    ![equations](https://latex.codecogs.com/svg.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20r%5E%7Bs%27s%7D_%7Bs%7D%20%3D%20%5Cmu%20_s%20-%20C%5E%7BT%7D_%7Bs%27s%7D%5Cmu%20_%7Bs%27%7D)

Repeat until convergence.



