FROM ubuntu:latest
LABEL authors="emreugur"

ENTRYPOINT ["top", "-b"]