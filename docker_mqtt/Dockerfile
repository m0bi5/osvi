FROM arm32v7/python:3.7-buster
COPY . /server
WORKDIR /server
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["clientForServer.py"]
