import paramiko
from pwinput import pwinput

host = ""
port = 22

username = input("username:")
password = pwinput()

command = "whoami"


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

#exec command
stdin, stdout, stderr = ssh.exec_command(command)

lines = stdout.readlines()

print(lines)