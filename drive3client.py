import httplib2
import io
from apiclient.http import MediaIoBaseDownload, MediaFileUpload

from .authorize import get_credentials
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
        # http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', credentials=credentials)
    

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
    
    def download_file(self, file_id, filename, mime_type):
        """
        Function to download file using the given file id
        :params file_id: file id get from google 
        :return file
        """
        request = self.service.files().export_media(fileId=file_id, mimeType=mime_type)
        fh = io.FileIO(filename, "wb")
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print ("Download %d%%." % int(status.progress() * 100))

    
    def get_child(self, parent_id):
        """
        Function to list child files for given folder
        :params parent_id
        :return list of child
        """
        file_details = []
        page_token = None
        while True:
            query = "'{}' in parents".format(parent_id)
            response = self.service.files().list(q=query,
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name, mimeType)',
                                                    pageToken=page_token).execute()
            for file in response.get('files', []):
                file_details.append({"file_name": file.get("name"),
                "id": file.get("id"), "mime_type": file.get("mimeType")})
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return file_details
        


    def create_folder(self, folder_name, parent_folder_id=None):
        """
        Function to create folder inside drive
        :params folder_name: name of the folder to create
        :params parent_folder_id: Parent folder if any else None
        :return folder data
        """
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_folder_id:
            file_metadata['parents'] = [parent_folder_id]
        file = self.service.files().create(body=file_metadata).execute()
        print('Folder ID: %s' % file.get('id'))
        return file
    
    def create_file(self, file_name, path_to_file, parent_folder_id=None):
        """
        Function to create file inside drive
        :params file_name: Name of the file to create
        :params path_to_file: Full path to file
        :params parent_folder_id: Parent folder if any
        :return file details
        """
        file_metadata = {
            'name': file_name
        }
        if parent_folder_id:
            file_metadata["parents"] = [parent_folder_id]
        media = MediaFileUpload(path_to_file, resumable=True)
        file = self.service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
        print ('File ID: %s' % file.get('id'))
        return file

    def copy_file(self, file_id, parent_folder_id):
        """
        Function to copy a file from one location to other
        :params file_id: File id of the target file
        :params parent_folder_id: Final location of the file
        :return file details 
        """
        file = self.service.files().get(fileId=file_id,
                                         fields='parents').execute()
        file = self.service.files().update(fileId=file_id,
                                            addParents=parent_folder_id,
                                            fields='id, parents').execute()
        return file


    def move_file(self, file_id, parent_folder_id):
        """
        Function to move the file from one location to other
        :params file_id: File id of the target file
        :params parent_folder_id: Final location of the file
        :return file details
        """
        file = self.service.files().get(fileId=file_id,
                                         fields='parents').execute()
        previous_parents = ""
        if file.get("parents"):
            previous_parents = ",".join(file.get('parents'))
        file = self.service.files().update(fileId=file_id,
                                            addParents=parent_folder_id,
                                            removeParents=previous_parents,
                                            fields='id, parents').execute()
        return file


    def copy_folder(self, folder_id, parent_folder_id):
        """
        Function to copy a folder from one location to other
        :params folder_id: File id of the target folder
        :params parent_folder_id: Final location of the file
        :return folder details 
        """
        file = self.service.files().get(fileId=folder_id,
                                         fields='parents').execute()
        file = self.service.files().update(fileId=folder_id,
                                            addParents=parent_folder_id,
                                            fields='id, parents').execute()
        return file


    def move_folder(self, folder_id, parent_folder_id):
        """
        Function to move the file from one location to other
        :params folder_id: File id of the target file
        :params parent_folder_id: Final location of the file
        :return file details
        """
        file = self.service.files().get(fileId=folder_id,
                                         fields='parents').execute()
        previous_parents = ""
        if file.get("parents"):
            previous_parents = ",".join(file.get('parents'))
        file = self.service.files().update(fileId=folder_id,
                                            addParents=parent_folder_id,
                                            removeParents=previous_parents,
                                            fields='id, parents').execute()
        return file


    def get_file_details(self, file_id):
        """
        Function get file using id
        :params file_id: File id
        :return file details
        """
        file = self.service.files().get(fileId=file_id).execute()
        return file
