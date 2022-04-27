from setuptools import setup, find_packages

setup(name='batchsolver',
      version='0.1',
      description='A simulation and analysis tool for TAP reactor systems',
      url='https://github.com/ayonge3/BATCHsolver',
      author='Adam Yonge',
      author_email='ayonge3@gatech.edu',
      license='MIT',
      packages=find_packages(),#['tapsolver'],
      install_requires=['fenics','dolfin-adjoint','imageio','pandas','matplotlib'],
      zip_safe=False)
