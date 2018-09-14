PyDriveV3 is a wrapper module for Google drive API v3 enabling easy server to server communication.
In order to use PydriveV3 with your application you need a Google service account. Please follow steps `here <https://support.google.com/a/answer/7378726?hl=en>`_ to create a service account.


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