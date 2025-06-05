from setuptools import setup, find_packages

setup(
    name='anarci-web',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'ANARCI @ git+https://github.com/oxpig/ANARCI.git'
    ],
    entry_points={
        'console_scripts': [
            'anarci-web=anarci_web.app:main'
        ]
    }
)
