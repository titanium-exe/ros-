import sys
if sys.prefix == '/root/myenv':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ubuntu/ros-/ros2_ws/install/my_robot_controller'
