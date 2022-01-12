from distutils.core import setup
setup(
  name = 'pyrelvis',
  packages = ['pyrelvis'], 
  version = '0.1',
  license='MIT',
  description = 'Pyrelvis is a simple binary relation visualizer',
  author = 'Robin Seidel',
  author_email = 'robin.seidel@tum.de',
  url = 'https://github.com/RobinSeidel/pyrelvis',
  download_url = 'https://github.com/RobinSeidel/pyrelvis/archive/v_01.tar.gz',
  keywords = ['relation', 'binary', 'visualizer', 'svg'],
  install_requires=[
          'pycairo',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3', 
  ],

