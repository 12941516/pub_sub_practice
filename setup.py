from setuptools import find_packages, setup

package_name = 'pub_sub_practice'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rtree',
    maintainer_email='rtree@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'pub1 = pub_sub_practice.pub1:main',
            'sub1 = pub_sub_practice.sub1:main',
            'sub2 = pub_sub_practice.sub2:main',
            'sub3 = pub_sub_practice.sub3:main',
            'pubsub12 = pub_sub_practice.pubsub12:main',
            'pubsub21 = pub_sub_practice.pubsub21:main',
            'game = pub_sub_practice.game:main',
        ],
    },
)
