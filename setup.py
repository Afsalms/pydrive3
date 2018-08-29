from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='pydriveV3',
    url='https://github.com/Afsalms/pydrive3',
    author='AfsalSalim',
    author_email='afsalms93.mec@gmail.com',
    # Needed to actually package something
    packages=['pydriveV3'],
    # Needed for dependencies
    install_requires=['cachetools','google-api-python-client',
                      'google-auth','google-auth-httplib2','httplib2',
                      'pyasn1','pyasn1-modules','rsa','six','uritemplate'],
    version='0.1.1',
    description='A package that wrap over the google drive v3 apis',
    long_description= open('README.rst').read()
)
