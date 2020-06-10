FROM python:3.7
COPY . /server
WORKDIR /server
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["clientForServer.py"]
