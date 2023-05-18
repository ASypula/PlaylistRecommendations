# start by pulling the python image
FROM python:3.10-buster

# copy the requirements file into the image
COPY ./requirements.txt /requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY ./app /app
COPY ./IUM_Zad_03_01_v4 /IUM_Zad_03_01_v4

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app/main.py" ]
