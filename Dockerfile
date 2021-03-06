FROM python:3

WORKDIR /usr/src/app

RUN pip3 install --upgrade pip &&\
    pip3 install pandas pytest-shutil

COPY . .

CMD [ "python", "./tests.py" ] 