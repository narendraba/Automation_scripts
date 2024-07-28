import paramiko
from scp import SCPClient

# Replace these with your EC2 instance details
EC2_HOST = '34.228.241.67'
EC2_PORT = 22
EC2_USER = 'ubuntu'  # Default username for Ubuntu instances
EC2_KEY_FILE = 'C:\\Users\\ballipallin\\Downloads\\Jenkins_setup_T1.pem'  # Path to your private key file

# Local file paths and remote destination path
LOCAL_FILES = ["SCP_files.py"]
REMOTE_DIR = '/home/ubuntu/Automation_scripts/python/installation_scripts'  # Directory on EC2 instance to store files

def create_ssh_client(hostname, port, username, key_file):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=port, username=username, key_filename=key_file)
    return ssh

def transfer_files(ssh_client, local_paths, remote_dir):
    with SCPClient(ssh_client.get_transport()) as scp:
        for local_path in local_paths:
            remote_path = f"{remote_dir}/{local_path.split('/')[-1]}"  # Construct remote file path
            scp.put(local_path, remote_path)
            print(f"File {local_path} successfully transferred to {remote_path}")

if __name__ == "__main__":
    try:
        ssh_client = create_ssh_client(EC2_HOST, EC2_PORT, EC2_USER, EC2_KEY_FILE)
        transfer_files(ssh_client, LOCAL_FILES, REMOTE_DIR)
        ssh_client.close()
    except Exception as e:
        print(f"An error occurred: {e}")
