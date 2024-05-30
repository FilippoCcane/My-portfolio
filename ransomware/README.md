## Disclaimer

This script is for educational purposes only. I do not take any responsibility for how you choose to use it. Please use this script responsibly and only on systems that you are authorized to access.
Please note that hacking into systems without permission is illegal and unethical. Make sure you have permission from the system owner before running this script.
I am not responsible for any misuse of this script. Use at your own risk.

## OS support
1. Windows

## Dependencies
import tkinter as tk
from tkinter import messagebox
import os
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import random 
import string
import shutil
from psutil import boot_time
import time
