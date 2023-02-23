FROM python:3.8
# set work directory
WORKDIR /usr/src/app/
# copy project
COPY . /usr/src/app/
# install dependencies
RUN pip3 install -r requerements.txt
# run app
CMD ["python", "main.py"]