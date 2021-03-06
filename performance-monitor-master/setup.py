from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="performance-monitor",
    version="0.0.1",
    description="Simple Decorator to check the time took by a function to get executed.",
    py_modules=["performance_monitor"],
    package_dir={'': "src"},
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Raj Aryan",
    author_email="mrajaryan349@gmail.com",
    url="https://github.com/imRajAryan09/Python/tree/main/performance-monitor-master"
)
