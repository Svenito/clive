from setuptools import setup


requires = ['colorama', 'requests', 'websocket-client']
try:
    import html
except ImportError:
    requires.append('html')

setup(
    name='CLIve',
    version='0.0.6',
    author='Sven Steinbauer',
    author_email='sven@unlogic.co.uk',
    maintainer='Sven Steinbauer',
    packages=['clive'],
    scripts=['bin/clive'],
    url='https://github.com/Svenito/clive',
    license='MIT',
    description='Follow Reddit live feeds from your terminal.',
    long_description=open('README.md').read(),
    install_requires=requires
)
