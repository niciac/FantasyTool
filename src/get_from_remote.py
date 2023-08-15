import pysftp
from urllib.parse import urlparse
from pathlib import Path as path
from my_logger import MyLogger
import yaml
import sys


class SFTP:
    def __init__(self, hostname, username, password, port=22):
        """Constructor Method"""
        # Set connection object to None (initial value)
        self.connection = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        """Connects to the sftp server and returns the sftp connection object"""

        try:
            # Get the sftp connection object
            self.connection = pysftp.Connection(
                host=self.hostname,
                username=self.username,
                password=self.password,
                port=self.port,
            )
        except Exception as err:
            logger.debug(Exception(err))
            raise Exception(err)
        finally:
            logger.info(f"Connected to {self.hostname} as {self.username}.")

    def disconnect(self):
        """Closes the sftp connection"""
        self.connection.close()
        logger.info(f"Disconnected from host {self.hostname}")

    def listdir(self, remote_path):
        """lists all the files and directories in the specified path and returns them"""
        for obj in self.connection.listdir(remote_path):
            yield obj

    def listdir_attr(self, remote_path):
        """lists all the files and directories (with their attributes) in the specified path and returns them"""
        for attr in self.connection.listdir_attr(remote_path):
            yield attr
    
    def delete_all_from_remote(self, remote_path:str|path):
        count=0
        for file in self.listdir_attr(remote_path):
            self.connection.remove(str(path(remote_path,file.filename)))
            logger.debug(f"{file.filename} deleted.")
            count+=1
        if count==0:
            logger.info(f"No files found on {self.hostname}")
        logger.info(f"{count} {'file' if count==1 else 'files'} deleted from {self.hostname}")

    def delete_file_from_remote(self, remote_file_path):
        self.connection.remove(str(remote_file_path))
        logger.info(f"{remote_file_path} deleted from remote.")

    def delete_duplicates(self, remote_path, local_path):
        count=0
        for file in self.connection.listdir_attr(remote_path):
            logger.debug(f"Checking {file.filename}")
            if path(local_path, file.filename).exists:
                self.delete_file_from_remote(remote_path)
                count+=1
        if count==0:
            logger.info(f"No duplicates found on {self.hostname}")
        logger.info(f"{count} {'file' if count==1 else 'files'} deleted from {self.hostname}")


    def download(self, remote_path:str|path, local_path:str|path, /, delete:bool=False):
        """
        Downloads the file from remote sftp server to local.
        Also, by default extracts the file to the specified local_path
        """

        try:
            logger.info(f"Downloading from {self.hostname} as {self.username}")
            logger.info(f"remote path: {remote_path}")
            logger.info(f"local path: {local_path}")

            # Create the target directory if it does not exist
            if not isinstance(local_path,path):
                local_path = path(local_path)
            if not (local_path.exists() and local_path.is_dir()):
                local_path.mkdir(parents=True)
                logger.info(f"{local_path} successfully created.")

            # Download from remote sftp server to local
            count=0
            for obj in self.connection.listdir_attr(remote_path):
                if path(local_path, obj.filename).exists():
                    continue
                else:
                    self.connection.get(
                        str(path(remote_path, obj.filename)),
                        str(path(local_path, obj.filename)),
                    )
                    logger.debug(f"{obj.filename} downloaded successfully!")
                    if delete:
                        self.delete_file_from_remote(path(remote_path,obj.filename))
                    count+=1

            if count>=1:
                logger.info(f"{count} {'file' if count==1 else 'files'} downloaded from {self.hostname}")
            else:
                logger.info("No files downloaded")

        except Exception as err:
            raise Exception(err)

    def upload(self, source_local_path, remote_path):
        """
        Uploads the source files from local to the sftp server.
        """

        try:
            logger.info(f"Uploading to {self.hostname} as {self.username}")
            logger.info(f"remote path : {remote_path}")
            logger.info(f"local path: {local_path})")

            # Upload file from SFTP
            self.connection.put(source_local_path, remote_path)
            logger.info(f"Files uploaded to {self.hostname}")

        except Exception as err:
            raise Exception(err)
        
def menu(options):
    print("\n"," Options ".center(20,'='), "\n")
    for count, option in enumerate(options):
        print(f"{count+1}.{option}")
    print("\n",30*"=")
    logger.info("Select option: ")
    selection = int(input())-1
    logger.info(f"Selected: {options[selection]}")
    return options[selection]
        


if __name__ == "__main__":

    logger = MyLogger("SFTP", level="DEBUG")
    logger.add_file_handler(filename="log.log")
    logger.add_stream_handler(level="INFO")

    logger.info(" NEW LOG ".center(20, "="))

    try:
        with open("personal_config.yml") as config:
            data_collection = yaml.safe_load(config)["data_collection"]
            logger.debug(f"Collected the following info: {data_collection}")
            sftp_url, remote_path, local_path = data_collection.values()
    except Exception as e:
        logger.error(e)
        sys.exit()

    parsed_url = urlparse(sftp_url)

    sftp = SFTP(
        hostname=parsed_url.hostname,
        username=parsed_url.username,
        password=parsed_url.password,
    )

    # Connect to SFTP
    sftp.connect()

    options = ['download','download & delete','delete duplicates','delete all from remote','exit']

    while True:
        match menu(options):
            case 'download':
                sftp.download(remote_path, local_path, delete=False)
            case 'download & delete':
                sftp.download(remote_path, local_path, delete=True)
            case 'delete duplicates':
                sftp.delete_duplicates(remote_path, local_path)
            case 'delete all from remote':
                sftp.delete_all_from_remote(remote_path)
            case 'exit':
                sftp.disconnect()
                sys.exit()
