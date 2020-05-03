import os

from setuptools import setup, find_packages

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pyGLMHMM',
      version='0.1',
      description='GLMHMM',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/janclemenslab/pyGLMHMM',
      author='Aslan Satary Dizaji',
      author_email='a.satarydizaji@eni-g.de',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=['scikit-learn', 'numpy', 'scipy', 'torch'],
      include_package_data=True,
      zip_safe=False
      )