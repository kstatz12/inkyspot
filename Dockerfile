FROM python:latest

RUN pip3 install spotipy
RUN pip3 install bottle

RUN mkdir -p /app
WORKDIR /app

COPY . /app

EXPOSE 8080

ENTRYPOINT ["python3", "web.py"]
