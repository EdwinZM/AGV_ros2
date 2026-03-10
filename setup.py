from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'AGV_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'description'), glob('description/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='edwin-zwanenburg',
    maintainer_email='edwinzwa@hotmail.com',
    description='Adaptive Robotics AGV Challenge ROS2 Package',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'AGV_tf2 = AGV_ros2.AGV_tf2:main',
            'static_base_tf = AGV_ros2.static_base_tf:main',
            'static_lidar_tf = AGV_ros2.static_lidar_tf:main',
            'odom_tf = AGV_ros2.odom_tf:main',
        ],
    },
)
