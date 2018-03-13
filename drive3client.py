import httplib2

from authorize import get_credentials
from apiclient import discovery



class Client():

    def __init__(self, credential_file, scopes):
        credentials = get_credentials(credential_file, scopes)
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=http)
    

    def get_all_files(self):
        file_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="mimeType != 'application/vnd.google-apps.folder'",
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                file_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return file_details
    
    def get_all_folder(self):
        folder_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="mimeType = 'application/vnd.google-apps.folder',
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                folder_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return folder_details

