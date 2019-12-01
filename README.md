
# BE_ALL_EAR9

## Execution process

Connect Raspberry Pi and Computer to the Same Wifi

### in Raspi

voice recording 
in recoding dir
```sh
python3 trecorder.py <computer ip>
```

receive voice output.txt
in speech_to_text dir
```sh
python3 recv_output.py <raspi ip>
```

analysis output
in gui dir
```sh
python3 inter.py
```

### in Computer

receive wav file
in speech_to_text dir
```sh
python3 recv_wav.py <computer ip>
```

speech to text and send output
in docker
```sh
python3 docker_main.py
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
please append volume directory 'speech_to_text/flac_set' 
