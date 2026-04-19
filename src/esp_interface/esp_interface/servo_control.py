#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial
 
class ServoNode(Node): 
    def __init__(self):
        super().__init__("servo_control")
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)
        self.subscription = self.create_subscription(Int32, 'servo_angle', self.angle_callback, 10)
        self.get_logger().info("Node has been activated")

    def angle_callback(self, msg):
        angle = msg.data
        angle = max(0, min(180, angle))
        cmd = f"{angle}\n"
        self.ser.write(cmd.encode())
 
 
def main(args=None):
    rclpy.init(args=args)
    node = ServoNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
