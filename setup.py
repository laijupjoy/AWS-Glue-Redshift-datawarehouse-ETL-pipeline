from setuptools import find_packages, setup

setup(
    name='glue-redshift',
    version='4.0.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='Amazon Software License 1.0',
)