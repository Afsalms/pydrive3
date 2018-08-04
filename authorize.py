
import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage



def get_credentials(client_secret_file, scopes):
    """
    Method for getting the credentails from the client secret json dowloaded 
    from google developer console
    :params client_secret_file: Path to the client secret file
    :params scopes: Scopes for the credentials
    :return credentials
    """
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'pydrive3-secret.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, scopes)
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
    return credentials
