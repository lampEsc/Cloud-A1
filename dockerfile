FROM python:latest


#Labels as key value pair
LABEL Maintainer="schuch"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /Users/Schuch/OneDrive/Documents/YEAR3/Cloud Computing

#to COPY the remote file at working directory in container
COPY main.py ./

CMD [ "python", "./main.py"]