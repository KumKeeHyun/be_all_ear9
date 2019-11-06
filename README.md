
# The-Gasero


## How to send pull request

create new branch in your forked repository

```sh

git checkout -B 'new-branch-name' 

```

add upstream (KumKeehyun/The-Gasero) to your working environment

```sh

git remote add https://github.com/KumKeeHyun/The-Gasero.git

```

send pull request at the github web interface

wait your pull request to be merged

update your forked repository from original repository

```sh

git checkout master 

git pull upstream/master

```


## How to reset commit in your machine

```sh

git reset --hard HEAD~n # restore 'n' steps back

```

## How to install docker and make container(Speech-to-Text-wavenet) in linux

install curl

```sh

sudo apt install curl

```

install docker

```sh

curl -fsSL https://get.docker.com/ | sudo sh

```

when you exec docker, you must use sudo with docker command

download speech-to-text image
image file size will very large... maybe 1.8GB??

```sh

sudo docker pull buriburisuri/speech-to-text-wavenet

```

check image

```sh

sudo docker image ls

```

run docker container - interactive mode

```sh

sudo docker run -it buriburisuri/speech-to-text-wavenet

```

in docker container execute speech-to-text

```sh

python recognize.py --file 

python recognize.py --file asset/data/LibriSpeech/test-clean/1089/134686/1089-134686-0000.flac

```
