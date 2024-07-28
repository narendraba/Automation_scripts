import paramiko

# Replace these with your EC2 instance details
EC2_HOST = "34.228.241.67"
EC2_PORT = 22
EC2_USER = 'ubuntu'  # Default username for Ubuntu instances
EC2_KEY_FILE = "C:\\Users\\ballipallin\\Downloads\\Jenkins_setup_T1.pem"

# Commands to uninstall Jenkins on the EC2 instance
commands = [
    'sudo systemctl stop jenkins',
    'sudo apt-get remove --purge -y jenkins',
    'sudo apt-get autoremove -y',
    'sudo apt-get autoclean'
]

def uninstall_jenkins_on_ec2():
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the EC2 instance
    ssh.connect(hostname=EC2_HOST, port=EC2_PORT, username=EC2_USER, key_filename=EC2_KEY_FILE)

    # Execute each command
    for command in commands:
        print(f"Executing command: {command}")
        stdin, stdout, stderr = ssh.exec_command(command)
        stdout.channel.recv_exit_status()  # Wait for the command to complete
        print(stdout.read().decode())
        print(stderr.read().decode())

    # Close the connection
    ssh.close()

if __name__ == "__main__":
    uninstall_jenkins_on_ec2()
