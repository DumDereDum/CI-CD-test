FROM python:3

WORKDIR /usr/src/app

RUN pip3 install --upgrade pip &&\
    pip3 install pandas pytest-shutil &&\
    pip3 install pycodestyle 

COPY . .

RUN python3 -m pycodestyle DataBase.py 

CMD [ "python", "./tests.py" ]