import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster 
from tf_transformations import quaternion_from_euler

class StaticBaseTf(Node):
    
    def __init__(self):
        super().__init__('static_base_tf')
        broadcaster = StaticTransformBroadcaster(self)
        
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        
        t.header.frame_id = 'base_footprint'
        t.child_frame_id = 'base_link'
        
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.10 
        
        q = quaternion_from_euler(0, 0, 0)
        
        t.transform.rotation.x = q[0] 
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        
        broadcaster.sendTransform(t)
        
        self.get_logger().info("base_footprint -> base_link published")
        
def main():
    rclpy.init()
    node = StaticBaseTf()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
