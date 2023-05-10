from setuptools import setup

package_name = 'py_service_client'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='SSKlearns',
    maintainer_email='sarveshshashikumar0908@gmail.com',
    description='Python client server tutorial from docs',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = py_service_client.service_member_function:main',
            'client = py_service_client.client_member_function:main'
        ],
    },
)
