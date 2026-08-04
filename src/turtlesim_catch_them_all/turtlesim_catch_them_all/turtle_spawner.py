#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
 
 
class TurtleSpawnerNode(Node): 
    def __init__(self):
        super().__init__("turtle_spawner")
        self.spawn_client_ = self.create_client(Spawn, "/spawn")

    def call_spawn_
 
 
def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
