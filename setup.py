from setuptools import setup, find_packages

setup(
    name='traffic-control',
    version='1.0.0',
    description='Smart city traffic management system',
    author='NeoVille Development Team',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'requests>=2.26.0',
    ],
    python_requires='>=3.7',
)