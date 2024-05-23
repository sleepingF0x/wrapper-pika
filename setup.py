from setuptools import setup, find_packages
from w_pika import __version__


setup(
    name="wrapper_pika",
    packages=find_packages(),
    version=__version__,
    license="MIT",
    description="Adapter for RabbitMQ pika",
    author="sleepingF0x",
    author_email="agent.999th@gmail.com",
    url="https://github.com/sleepingF0x/wrapper-pika",
    keywords=["pika", "rabbitmq"],
    install_requires=[
        "pika>=1.3.2",
        "retry>=0.9.2",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    project_urls={
        'Home': 'https://github.com/sleepingF0x/wrapper-pika',
        'Documentation': 'https://github.com/sleepingF0x/wrapper-pika/blob/master/README.MD',
        'Issue Tracker': 'https://github.com/sleepingF0x/wrapper-pika/issues',
        'Source': 'https://github.com/sleepingF0x/wrapper-pika',
        'Download': 'https://pypi.org/project/wrapper-pika',
    }
)
