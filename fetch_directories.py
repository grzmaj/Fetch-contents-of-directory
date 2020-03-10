import pysftp
from datetime import datetime

# Settings
sftp_accounts = {
    'login1': 'password1',
    }
known_hosts = "C:\\Users\\User\\Desktop\\known_hosts" # Remember to add TWO backslashes instead of one if you're using Windows
server = "something.com"
port = 22


cnopts = pysftp.CnOpts(knownhosts=known_hosts)

for login, password in sftp_accounts.items():
    with pysftp.Connection(host=server, port=port, username=login, password=password, cnopts=cnopts) as sftp:
        file_structure = sftp.listdir_attr()
        print ("Account: " + login)
        print ("------------------")
        for attribute in file_structure:
            print (attribute.filename, " (Size:", attribute.st_size, ", Last modified:", datetime.utcfromtimestamp(attribute.st_mtime).strftime('%Y-%m-%d %H:%M:%S'), ")")
        print ("------------------\n\n")
