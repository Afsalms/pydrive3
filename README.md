# pydrive3
## this app is in development stage. Please test properly before deploy in production

Python wrapper for google drive (v3). 

## Installation

### Requirements
* Python 
* Developer Account in google

`$ pip install fooba`

## Usage

```python
from pydrive3 import Client

client = Client('service_crendetil.json') #path to credential from google
files = client.get_all_files() #list the file shared or owned by the service account
```

## Development
```
$ virtualenv foobar
$ . foobar/bin/activate
$ pip install -e .
```

## Contributing
Pull requests are welcome.
