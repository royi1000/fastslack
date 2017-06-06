from distutils.core import setup

setup(
  name='fastslack',
  packages=['fastslack'], # this must be the same as the name above
  version='0.0.1',
  description='send fast slack message',
  author='Royi Reshef',
  url='https://github.com/royi1000/fastslack',
  download_url='https://github.com/royi1000/fastslack/archive/latest.tar.gz',
  keywords=['cli', 'slack', 'message'],
  classifiers=[],
  install_requires=[
      'slackclient',
    ],
  entry_points={
      'console_scripts': [
          'fastslack=fastslack.main:main',
      ],
  },
)
