 # publisher and subscriber:
  This project is to make publisher code and subscriber code 
  
  # installation: 
  * ROS noetic.
  
 
 
 ## How to create Package
 The following steps are about how to creat ROS packge inside a catkin workspace:
 * **open yor cmd and creat the folder in any location you want:**
  	 * ` cd Document `
  	 * ` mkdir catkin_ws ` // this represent the name of your workspace
  	 * ` cd catcin_ws ` // change directory to that folder
  	 * ` mkdir src ` // make folder with src name to containe ROS packge
  	 * ` cd src ` // change directory to src folder 
  	 * ` catkin_init_workspace ` // initilize the src as workspace 
  	 * ` ls ` // list out to insure there is new file with name **CMakeLists.txt**
 * **to compile your workspace:**
 	* ` cd .. `  //  navigate directory to **catkin_ws**
 	* ` catkin_make ` // to start the build process 
 	* ` ls ` // list out to make sure there are to folder builded **build** and **devel**
 * **creat ROSpackge:**
 	* ` cd src ` // move to src src folder 
 	* ` catkin_create_pkg robot_tutorials rospy roscpp std_msgs ` // **robot_tutorials** is the name of the ras package.  **rospy** to write a python code. **roscpp** to write c++ code. **std_msgs** to refer to the standard mesages types that devel will use such as **int8** **int16** **string** **bool**
 	*  ` ls ` to make sure there is a new packge called **robot_tutorials**
 	* ` ls /robot_tutorials ` // make sure it containe **CMakeLists** , **include** , **package.xml** and **src**
 	*  ` cd .. ` // navigate to the workspace **catkin_ws**
 	* ` catkin_make ` // build the workspace withe the new packges inside 
 ## How to make Publisher Code
 * navigate the directory to **robot_tutorials** folder 
 * create new folder wih **scripts** name
 * write the Publisher code
 * open the termenal and write `roscore` to start the master node
 * open new window of terminal and navigate the directory to scripts folder 
 * write `chmod +x publiserCode.py`  to chaneg the premissions of file 
 * `python3 publiserCode.py` to run the code and you will get the results as you see in **publisherCodeResults** image, there is 10 mesages/sec
 * write `rosnode info /catkinE` to observe the ros node publishing the message as you see in **rosnode_info** image
 * write`rosrun rqt_graprh rqt_graph` to see the node and publishing as graph inetially the node without any subscription  as you see in **befor_echo** image
 *  write`rostopic echo  /hello` you will see the publisher and subscriber as **after_echo** image 
  ## How to make Subcriber Code:
  * navigate the directory to Scribt file and write the code inside it
  * change the premissions as you made with the publisher code
  * run it and open the rqt_graph
  * there is just one node as you see in **subscriberCodeRunning** image 
  
  ## How to make subscriber Code to listen to the publisher:
  
   * open new window of terminal and navigate the directory to scripts folder
   * the result will be as **finalResuolt** image 
   
  

  
  
 	
  	 
  
