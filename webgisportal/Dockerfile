FROM python:3.8-buster
ADD . /code
WORKDIR /code
RUN apt-get update

RUN apt-get install -y python-numpy python-gdal
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal

RUN pip install -r requirements.txt
RUN chmod +x start_django.sh
CMD ["./start_django.sh"]