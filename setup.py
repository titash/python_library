from setuptools import find_packages, setup

setup(
    name='sample_python_lib',
    packages=find_packages(include=['sample_python_lib']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)