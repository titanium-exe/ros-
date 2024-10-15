#!/usr/root/myenv/python3

import rclpy
from  rclpy.node import Node

class PoseSubNode(Node):
    def __init__(self):
        super().__init("pose_subscriber")
        self.pose_subscriber_ = self.create_subscription()

def main(args = None):
    rclpy.init(args=args)
    rclpy.shutdown()
