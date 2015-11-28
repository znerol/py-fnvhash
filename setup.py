from setuptools import setup

setup(
    name='fnvhash',
    version='0.1.0',
    description='Pure Python FNV hash implementation',
    author='Lorenz Schori',
    author_email='lo@znerol.ch',
    url='https://github.com/znerol/py-fnvhash',
    packages=['fnvhash'],
    test_suite="fnvhash.test",
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
