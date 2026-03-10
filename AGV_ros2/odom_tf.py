import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

class OdomTF(Node):
    
    def __init__(self):
        super().__init__('odom_tf')
        
        self.br = TransformBroadcaster(self)
        
        self.sub = self.create_subscription(
            Odometry,
            '/odom',
            self.callback,
            10)
            
    def callback(self, msg):
        
        t = TransformStamped()
        
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_footprint'
        
        t.transform.translation = msg.pose.pose.position
        t.transform.rotation = msg.pose.pose.orientation
        
        self.br.sendTransform(t)
        
def main():
    rclpy.init()
    node = OdomTF()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
