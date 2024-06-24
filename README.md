# EmailServer

Email server using SMTP protocols.

## Usage
1. Update your configuration in `config.json`.
2. Build the docker image.
```
docker build -t emailserver .
```
3. Run the docker container.
```
docker run emailserver
```
4. Or set the crontab as you wish.
```
crontab -e
```
```
docker run emailserver
00 08 * * 1-5 docker run auto-punch-in>/home/weber50432/auto_punch/log/in.log 2>&1
20 17 * * 1-5 docker run auto-punch-out>/home/weber50432/auto_punch/log/out.log 2>&1
```