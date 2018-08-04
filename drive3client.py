import httplib2

from authorize import get_credentials
from apiclient import discovery



class Client():
    
    """
    Google drive3 client object
    """

    def __init__(self, credential_file, scopes):
        """
        Creates new drive3 client object using the given credentails
        :params credential_file: full path to the credentials.json file
        :params scopes: Scope for the access token
        """
        credentials = get_credentials(credential_file, scopes)
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=http)
    

    def get_all_files(self):
        """
        Fetch all the files from drive
        :return list of files
        """
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
        """
        Fetch all the folders from drive
        :return list of folders
        """
        folder_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="mimeType = 'application/vnd.google-apps.folder'",
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                folder_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return folder_details


    def get_starred_folder(self):
        """
        Fetch all the starred folder from google drive
        :return list of folders
        """
        folder_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="starred = True and mimeType = 'application/vnd.google-apps.folder'", 
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                folder_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return folder_details
    

    def get_starred_files(self):
        """
        Fetch all the starred files from drive
        :return list of files
        """
        file_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="starred = True and mimeType != 'application/vnd.google-apps.folder'", 
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                file_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return file_details
    

    def get_trashed_folder(self):
        """
        Fetch all trashed folder
        :return list of folders
        """
        folder_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="trashed = True and mimeType = 'application/vnd.google-apps.folder'", 
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                folder_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return folder_details
    

    def get_trashed_files(self):
        """
        Fetch all the trashed files from drive
        :return list of files
        """
        file_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="trashed = True and mimeType != 'application/vnd.google-apps.folder'", 
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                file_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return file_details

    
    def get_shared_folder(self):
        """
        Fetch all folder shared with me
        :return list of folders
        """
        folder_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="sharedWithMe = True and mimeType = 'application/vnd.google-apps.folder'", 
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                folder_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return folder_details
    

    def get_shared_file(self):
        """
        Fetch all the files shared with me
        :return list of files
        """
        file_details = []
        page_token = None
        while True:
            response = self.service.files().list(q="sharedWithMe = True and mimeType != 'application/vnd.google-apps.folder'", 
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                file_details.append({"file_name": file.get("name"), "id": file.get("id")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return file_details