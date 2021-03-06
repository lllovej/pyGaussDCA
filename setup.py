#!/usr/bin/env python
# encoding: UTF-8

from setuptools import setup, find_packages, dist

# Declare the dependency
dist.Distribution(dict(setup_requires='pythran'))

# Pythran modules
from pythran import PythranExtension

module_parse = PythranExtension('gaussdca._load_data', sources=['src/gaussdca/_load_data.py'])
module_gdca = PythranExtension('gaussdca._gdca', sources=['src/gaussdca/_gdca.py'],
                               extra_compile_args=['-fopenmp', '-ftree-vectorize'],
                               extra_link_args=['-fopenmp'])

# Main setup:
setup(name='pyGaussDCA', version='0.1.4',
      description='Fast implementation of GaussDCA',
      url='https://github.com/ElofssonLab/pyGaussDCA/',
      author='David Menéndez Hurtado',
      author_email='davidmenhur@gmail.com',
      license='GPLv3',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      package_data={'gaussdca.data': ['tests/data/*.a3m']},
      include_package_data=True,
      ext_modules=[module_parse, module_gdca],
      install_requires=['numpy', 'scipy', 'pythran>=0.8.6'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      classifiers=['Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Bio-Informatics',
                   'Intended Audience :: Science/Research'],
      zip_safe=False)
