from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name='tengri',
    version='0.1',
    packages=find_packages,
    url='https://github.com/leopepe/tengri',
    license='Simplified BSD',
    author='Leonardo Pepe',
    author_email='lpepefreitas@gmail.com',
    description='AWS Tool to stop all instances (accept exclusion list)',
    zip_safe=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': ['tengri = tengri.__main__:main'],
        'setuptools.installation': ['eggsecutable = tengri.__main__:main'],
    }
)
