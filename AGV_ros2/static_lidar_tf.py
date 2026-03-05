import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from tf_transformations import quaternion_from_euler

class StaticLidarTf(Node):
    
    def __init__(self):
        super().__init__('static_lidar_tf')
        broadcaster = StaticTransformBroadcaster(self)
        
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        
        t.header.frame_id = 'base_link'
        t.child_frame_id = 'scan'
        
        t.transform.translation.x = 0.20
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.15
        
        q = quaternion_from_euler(0, 0, 0)
        
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        
        broadcaster.sendTransform(t)
        
        self.get_logger().info("base_link -> scan published")
        
def main():
    rclpy.init()
    node = StaticLidarTf()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
