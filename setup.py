from distutils.core import setup

setup(
    name='CLIve',
    version='0.0.5',
    author='Sven Steinbauer',
    author_email='sven@unlogic.co.uk',
    maintainer='Sven Steinbauer',
    packages=['clive'],
    scripts=['bin/clive'],
    url='https://github.com/Svenito/clive',
    license='MIT',
    description='Follow Reddit live feeds from your terminal.',
    long_description=open('README.md').read(),
    install_requires=[
		"colorama",
		"html",
		"requests",
		"six",
		"websocket-client"
    ],
)
