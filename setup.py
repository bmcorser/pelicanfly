from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pelicanfly',
      version='0.1',
      description='Font Awesome from inside a Pelican',
      long_description=readme(),
      url='http://bmcorser.github.com/pelicanfly',
      author='bmcorser',
      author_email='benmarshallcorser@gmail.com',
      license='GPL',
      packages=['pelicanfly'],
      install_requires=['pelican', 'markdown'],
      zip_safe=False)
