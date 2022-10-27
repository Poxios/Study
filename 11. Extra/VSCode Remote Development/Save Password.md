For those trying to connect through Vscode Remote SSH Extension steps provided at https://code.visualstudio.com/docs/remote/troubleshooting#_ssh-tips)

For Windows(Host) --> Linux(Remote)

1. Create an SSH .pub key in your windows ssh-keygen -t rsa -b 4096
2. Copy the contents of the .pub key (default path C:\Users\username/.ssh/id_rsa.pub)
3. SSH into Remote machine and append the contents of the pub key in authorized keys echo "pub-key" >> ~/.ssh/authorized_keys

* https://stackoverflow.com/questions/66113731/how-to-save-ssh-password-to-vscode