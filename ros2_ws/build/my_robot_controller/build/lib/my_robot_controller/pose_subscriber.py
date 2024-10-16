#!/usr/root/myenv/python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose  # Assuming you're subscribing to Pose messages

class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        # Replace with your topic
        self.subscription = self.create_subscription(
            Pose,
            '/pose_topic',  # Update this with the correct topic name
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received Pose: {msg.position.x}, {msg.position.y}, {msg.position.z}')

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

