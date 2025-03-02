from setuptools import setup, find_packages

setup(
    name="rotimeout_package",  # Package name
    version="0.1",  # Initial version
    packages=find_packages(),
    description="A Python package to simulate JavaScript's setTimeout function as roTimeOut.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rohan Poudel",
    author_email="yitsmerohan@gmail.com",
    url="https://github.com/RohanPoudel2024/rotimeout_package",  # Your GitHub link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
