# ADAPTIVE_TRAFFIC_LIGHT_SYSTEM

# ABOUT REPOSITORY

**what is the problem ?**

Traffic congestion lead to disorder on roads. Currently traffic signals have pre defined timers. Our approach is, to control the signals based on real time vehicle density thus saving time, resources and reducing pollution.One of the main reasons behind today’s traffic problem are the techniques that are used for traffic management. It has no emphasis on live traffic scenario, thus leading to inefficient traffic management systems.

If the traffic light timers are showing correct time to regulate the traffic, then the time wasted on unwanted green signals will be saved. Timer for every lane is the simplest way to control traffic. And if those timers are predicting exact time then automatically the system will be more efficient.


<img src="https://camo.githubusercontent.com/46eeb2384e8f7e1213475d5b1bfdb2404a2c9d81/68747470733a2f2f7777772e7472616e73706f72746174696f6e2e676f762f73697465732f646f742e676f762f66696c65732f322e6a7067"
     alt="https://camo.githubusercontent.com/46eeb2384e8f7e1213475d5b1bfdb2404a2c9d81/68747470733a2f2f7777772e7472616e73706f72746174696f6e2e676f762f73697465732f646f742e676f762f66696c65732f322e6a7067"
     style="float: left; margin-right: 10px;" />

     

# REQUIREMENTS
1. **TENSORFLOW**

2. **NUMPY**

3. **OPENCV**

4. **CVLIB**

5.**YOLO**

# DATA

1.[link of input folder](https://drive.google.com/drive/folders/1YVggbYVgH5hJkDFUYalSHz6rMXNl_SzM)

2.[link of output](https://drive.google.com/drive/folders/143wV-efr9zReXmo1BRLkcYUrFhRU5IyB)

# ROADMAP OF COUNTING.

1.**OpenCv approach**
Placing a Camera on each side of the intersection and Processing the images to get the number of vehicles on each side of the intersection .(BACKGROUND SUBTRACTOR)

The Image taken is processed :
1. Read using OpenCv Library in Python
2. resized according to need
3. Converted to Black and White 
4. Removing Gaussian Noise
5. Removing Salt and Pepper Noise 
6. Dilation
7. Take Difference from reference image 
8. Find the percentage change 
9. Get Number of Cars


2.**cvlib approach**
Placing a Camera on each side of the intersection and Processing the images to get the number of vehicles on each side of the intersection.

1. Read using OpenCv Library in Python.
2. resized according to need.
3. use cvlib to detect images(yolo weights).
4. get the count of vehicles using label list.

<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.analyticsvidhya.com%2Fblog%2F2018%2F12%2Fpractical-guide-object-detection-yolo-framewor-python%2F&psig=AOvVaw0RGc6eFoFwZDPZGWSh-Zt_&ust=1590934184574000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOD6hu7h2-kCFQAAAAAdAAAAABAM"
     alt="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.analyticsvidhya.com%2Fblog%2F2018%2F12%2Fpractical-guide-object-detection-yolo-framewor-python%2F&psig=AOvVaw0RGc6eFoFwZDPZGWSh-Zt_&ust=1590934184574000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOD6hu7h2-kCFQAAAAAdAAAAABAM"
     style="float: left; margin-right: 10px;" />

# How are these Numbers manipulated ??

Once stored in a list the number of cars are manipulated to clear the congestion as soon as possible .

**1st method**
**using variance of cars in all four lens**
1. count vehicles in all four lens.
2. calculate varience.
3. allotment of timings according to the varience.
[link of method](https://github.com/vr620/Adaptive_traffic_light_system/blob/master/varience_based.ipynb)

**2nd method**
**using profit loss method**
1. count vehicles in a single len.
2. calculate timing of that len.
3. calculate the profit gained from this cycle.
4. add the profit to the next len timing if that len is congested.
[link of method](https://github.com/vr620/Adaptive_traffic_light_system/blob/master/profit_loss_based_method.ipynb)


# Future Scope
1. Can be developed for three lanes of each side of the road ( Prototype Extended Version )
2. Can be moulded to be used in situations like mass evacuation
3. Linking of other traffic lights in sync to provide better congestion clearing
Can be developed further to be used by emergency vehicles to provide Green route and decreasing accidents on intersections.
5. repeat.




