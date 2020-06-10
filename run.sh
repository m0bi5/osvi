docker volume create --name sharedVol
docker run -d -v sharedVol:/shared m0bi5/mqtt:latest
docker run -d -v sharedVol:/shared -p 5000:5000 m0bi5/flask:latest
