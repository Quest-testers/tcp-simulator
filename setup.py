from setuptools import setup, find_packages 

setup(
    name='tcp_simulator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
         'requests',
         'numpy',
    ],
    entry_points={
        'console_scripts': [
            'tcp_server=tcp_simulator.server:start_server',
            'tcp_client=tcp_simulator.client:start_client'
        ]
    }
)
