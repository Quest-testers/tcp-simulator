from setuptools import setup, find_packages 

setup(
    name='tcp_simulator',                      
    version='1.0.0',                           
    packages=find_packages(),                  
    install_requires=[                         
        # List any dependencies here, for example:
        # 'requests', 'numpy', etc.
    ],
    entry_points={                             
        'console_scripts': [
            'tcp_server=tcp_simulator.server:start_server',  
            'tcp_client=tcp_simulator.client:start_client' 
        ],
    },
    #author='Your Name',                        # Your name as the author
    #author_email='your.email@example.com',     # Your email address
    description='A TCP simulator for server-client communication',  # A short description of your package
    #long_description=open('README.md').read(), # Long description read from the README file
    long_description_content_type='text/markdown',  # Format of the long description (Markdown)
    url='https://github.com/Quest-testers/tcp-simulator.git',  # URL for the project (GitHub repository)
    classifiers=[                              # Classifiers to categorize the project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                   # Specify the Python version compatibility
)

