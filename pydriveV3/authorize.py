
from google.oauth2 import service_account

def get_credentials(client_secret_file, scopes):
    """
    Method for getting the credentails from the client secret json dowloaded 
    from google developer console
    :params client_secret_file: Path to the client secret file
    :params scopes: Scopes for the credentials
    :return credentials
    """
    credentials = service_account.Credentials.from_service_account_file(client_secret_file,
        scopes=scopes)
    return credentials




