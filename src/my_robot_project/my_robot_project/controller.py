#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, JointState
from cv_bridge import CvBridge
import cv2

class UR5Controller(Node):
    def __init__(self):
        super().__init__('ur5_controller')
        
        self.subscription = self.create_subscription(Image, '/image_raw', self.image_callback, 10)
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        
        self.br = CvBridge()
        self.window_name = "Sterowanie UR5"
        self.current_frame = None
        
        # Prawdziwe nazwy stawów w UR5
        self.joint_names = [
            'shoulder_pan_joint', 
            'shoulder_lift_joint', 
            'elbow_joint', 
            'wrist_1_joint', 
            'wrist_2_joint', 
            'wrist_3_joint'
        ]
        
        # Pozycje początkowe (w radianach) - ustawiamy go w "neutralnej" pozycji
        self.joint_positions = [0.0, -1.57, 0.0, -1.57, 0.0, 0.0]
        
        self.target_direction = 0
        self.timer = self.create_timer(0.033, self.timer_callback)

    def image_callback(self, data):
        self.current_frame = self.br.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow(self.window_name, self.current_frame)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)
        cv2.waitKey(1)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.current_frame is None: return
            height, _, _ = self.current_frame.shape
            
            # GÓRA / DÓŁ steruje drugim stawem (shoulder_lift_joint)
            if y < height / 2:
                self.target_direction = 1 # Do góry
                self.get_logger().info("UR5: Podnoszenie")
            else:
                self.target_direction = -1 # W dół
                self.get_logger().info("UR5: Opuszczanie")

    def timer_callback(self):
        # Modyfikujemy tylko staw nr 1 (shoulder_lift_joint)
        step = 0.02
        idx = 1 
        
        if self.target_direction == 1:
            self.joint_positions[idx] -= step # W UR5 minus to często "w górę"
        elif self.target_direction == -1:
            self.joint_positions[idx] += step
            
        # Ograniczenia mechaniczne UR5 (w przybliżeniu)
        self.joint_positions[idx] = max(-3.14, min(0.0, self.joint_positions[idx]))
        
        self.target_direction = 0 

        # Wysyłanie wiadomości
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = self.joint_names
        msg.position = self.joint_positions
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = UR5Controller()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
