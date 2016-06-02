from setuptools import setup

setup(
    name="spm2olca",
    version="0.0.1",
    author="msrocka",
    author_email="michael.srocka@greendelta.com",
    description="SimaPro Method File to olca-schema converter",
    license="MIT",
    keywords="example documentation tutorial",
    url="http://packages.python.org/spm2olca",
    packages=['spm2olca'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'spm2olca = spm2olca:main',
        ]
    },
    package_data={'spm2olca': ["data/*.*"]},
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ]
)
