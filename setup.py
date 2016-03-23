from setuptools import setup


requires = ['colorama', 'requests', 'websocket-client']
try:
    import html
except ImportError:
    requires.append('html')

setup(
    name='CLIve',
    version='0.0.7',
    author='Sven Steinbauer',
    author_email='sven@unlogic.co.uk',
    maintainer='Sven Steinbauer',
    packages=['clive'],
    scripts=['bin/clive'],
    url='https://svenito.github.io/clive/',
    license='MIT',
    keywords=['reddit', 'live', 'news', 'stream'],
    description='Follow Reddit live feeds from your terminal.',
    long_description=open('README.md').read(),
    install_requires=requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
          ],


)
