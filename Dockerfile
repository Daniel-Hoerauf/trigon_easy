FROM python:2.7
ADD . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD gunicorn trigon:app -b 0.0.0.0:5000 -w $(nproc)
