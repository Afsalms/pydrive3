PydriveV3 is the module for access google drive from the server to server communication, We use Google service account for this.

Please click `here <https://gist.github.com/Afsalms/6f6c88d7f013d8e7336083152c3d3dda#file-steps-to-create-service-account-txt>`_
to get the step to create the service account

Requirements
------------------
- Python
- Developer account in google
- Service account key json

Installation
------------------
    $ pip install pydriveV3

Sample usage
------------------
    from pydriveV3 import Client

    client = Client('service_credentials.json')

    files = client.get_all_files()

Documentation
------------------

Please  `visit <https://gist.github.com/Afsalms/6fa6f747056af7d4e8274aec2e323e9e#file-pydrivev3documentation>`_
for documentation

Contribution
------------------
Pull requests are welcome.