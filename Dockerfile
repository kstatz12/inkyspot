FROM python:latest

RUN pip3 install spotipy
RUN pip3 install bottle

ENTRYPOINT ["python3" "web.py"]
