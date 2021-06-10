#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a zip file whose file name increments.

import zipfile
import os


def backup_to_zip(folder):
    # Backup the entire contents of the "folder" into a zip file.

    folder = os.path.abspath(folder)  # Make sure the folder path is absolute.

    # Figure out the filename this code should use based on
    # what files already exist.
    base_name = os.path.basename(folder)
    number = 1

    while True:
        zipfilename = base_name + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1

    # Create the zip file.
    print(f"Creating {zipfilename} ...")
    zip_file = zipfile.ZipFile(zipfilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for folder_path, subfolder_name, file_names in os.walk(folder):
        print(f'Adding files in {folder_path} ...')
        # Add the current folder to the Zip File.
        zip_file.write(folder_path)  # This line will add the folder even when it doesn't contain any files
        # If you remove this line, then  empty folders will not be zipped,
        # only folders containing some files will be created as they appear
        # in the path of the said file.

        # Add all the files in this folder to the ZIP file.
        for file_name in file_names:
            new_base = os.path.basename(folder) + '_'
            if file_name.startswith(new_base) and file_name.endswith('.zip'):
                continue  # Don't backup the Backup ZIP files
            zip_file.write(os.path.join(folder_path, file_name))
    zip_file.close()
    print('Done!')
