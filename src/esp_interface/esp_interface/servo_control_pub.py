#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ServoPub(Node): 
    def __init__(self):
        super().__init__("servo_control_pub") 
        self.publisher_ = self.create_publisher(Int32, 'servo_angle', 10)

        self.angle_ = 90
        self.step = 30

        self.create_timer(1.0, self.angle_publish)
        self.get_logger().info("Publisher node has been activated...")

    def angle_publish(self):
        msg = Int32()
        msg.data = self.angle_
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {self.angle_}')

        self.angle_ = 150 if self.angle_ == 90 else 90


 
def main():
    rclpy.init()
    node = ServoPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
