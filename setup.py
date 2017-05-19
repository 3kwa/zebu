from setuptools import setup


setup(
    name='zebu',
    version='2017.5.0',
    description='Uber minimalistic message bus using 0MQ',
    long_description=open("README.rst").read(),
    py_modules=['zebu'],
    author='Eugene Van den Bulke',
    author_email='eugene.vandenbulke@gmail.com',
    url='https://github.com/3kwa/zebu',
    install_requires=['pyzmq'],
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)