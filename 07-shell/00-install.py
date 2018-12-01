pt(){
	echo "$1 install complete!"
}


mysql_install(){
	sudo apt-get update && \
	sudo apt-get -y install mysql-server && \
	sudo apt-get -y install mysql-client && \
	sudo apt-get -y install libmysqlclient-dev
	pt "mysql"
	}
	
redis_install(){
	sudo apt-get update && \
	sudo apt-get -y install redis-server
	pt "redis"
}

docker_install(){
	sudo apt-get remove docker docker-engine docker.io
	sudo apt-get update && \
	sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common && \
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \
	sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable" && \
	sudo apt-get update && \
	sudo apt-get -y install docker-ce && \
	sudo usermod -a -G docker $USER && \
	pt "docker"
	sudo reboot
}

etcd_install(){
	ETCD_VER=v3.3.10

	GITHUB_URL=https://github.com/etcd-io/etcd/releases/download
	DOWNLOAD_URL=${GITHUB_URL}

	rm -f /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz
	rm -rf /tmp/etcd-download-test && mkdir -p /tmp/etcd-download-test

	curl -L ${DOWNLOAD_URL}/${ETCD_VER}/etcd-${ETCD_VER}-linux-amd64.tar.gz -o /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz
	tar xzvf /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz -C ./ --strip-components=1
	rm -f /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz
	mkdir download && mv * download 
	cd download
	./etcd --version
	ETCDCTL_API=3 ./etcdctl version
	pt "etcd"
}

python_install(){
	sudo apt-get -y install python && \
	sudo apt-get -y install python3 && \
	sudo apt-get -y install python-pip && \
	sudo apt-get -y install python3-pip && \
	sudo apt-get -y install vim && \
	sudo apt-get -y install bridge-utils
	pt "python"
}

docker_config(){
	docker pull python && \
	docker pull redis && \
	docker pull mysql && \
	docker pull ubuntu && \
	docker pull wordpress && \
	docker pull nginx && \
	docker pull busybox
	pt "docker config"
}


redis_install
etcd_install
python_install
# mysql_install
# docker_install
docker_config