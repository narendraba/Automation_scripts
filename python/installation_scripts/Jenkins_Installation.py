import os

def install_jenkins():
    # Update package lists and install Java (required for Jenkins)
    os.system('sudo apt update')
    os.system('sudo apt install -y default-jre')

    # Add Jenkins repository key and add Jenkins to the apt sources list
    os.system('wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -')
    os.system('sudo sh -c \'echo "deb https://pkg.jenkins.io/debian binary/" > /etc/apt/sources.list.d/jenkins.list\'')

    # Update package lists again to fetch Jenkins packages from the new repository
    os.system('sudo apt update')

    # Install Jenkins
    os.system('sudo apt install -y jenkins')

    # Start Jenkins service
    os.system('sudo systemctl start jenkins')

    # Enable Jenkins service to start on boot
    os.system('sudo systemctl enable jenkins')

if __name__ == "__main__":
    install_jenkins()
