import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Int32

class Pubsub12(Node):
    
    def __init__(self):
        super().__init__('pubsub12')
        self.publisher = self.create_publisher(Int32, 'topic2', 10)
        self.subscription = self.create_subscription(
            Int32,
            'topic1',
            self.callback,
            10
        )
        
    def callback(self, msg):
        time.sleep(1)
        self.get_logger().info(f'subscribed: {msg.data}')
        new_msg = Int32()
        new_msg.data = msg.data + 1
        self.publisher.publish(new_msg)

def main(args=None):
    rclpy.init(args=args)
    pubsub12 = Pubsub12()
    rclpy.spin(pubsub12)
    pubsub12.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
