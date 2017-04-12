FROM base_globonetworkapi:3.4.3

RUN mkdir /netapi
WORKDIR /netapi

ADD . /netapi/

CMD cd /netapi

EXPOSE 8000
EXPOSE 15672

RUN pip install -r requirements.txt
RUN pip install -r requirements_debug.txt
RUN pip install -r requirements_test.txt
RUN pip install virtualenv
RUN pip install virtualenvwrapper
RUN pip install gunicorn
