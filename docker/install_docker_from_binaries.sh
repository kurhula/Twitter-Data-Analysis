curl -o docker-19.03.9.tgz https://download.docker.com/linux/static/stable/x86_64/docker-19.03.9.tgz
7z x docker*.tgz
7z x docker*.tar
sudo chmod +x docker/*
sudo cp docker/* /usr/bin/
sudo groupadd docker
sudo usermod -aG docker $(whoami)
sudo dockerd &
