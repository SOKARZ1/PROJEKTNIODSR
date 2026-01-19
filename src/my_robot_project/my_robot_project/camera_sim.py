#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class CameraSimulator(Node):
    def __init__(self):
        super().__init__('camera_simulator')
        
        self.publisher_ = self.create_publisher(Image, '/image_raw', 10)
        self.timer = self.create_timer(0.033, self.timer_callback) 
        self.br = CvBridge()
        self.get_logger().info('Symulator kamery uruchomiony.')

    def timer_callback(self):
       
        img = np.zeros((480, 640, 3), np.uint8)
        
        
        cv2.line(img, (0, 240), (640, 240), (0, 255, 255), 2)
        
        
        cv2.putText(img, "STREFA JAZDY DO PRZODU", (180, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(img, "STREFA JAZDY DO TYLU", (200, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        
        msg = self.br.cv2_to_imgmsg(img, encoding="bgr8")
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CameraSimulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
