FROM python:3.9-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY /src /app
COPY gunicorn.conf.py /app
WORKDIR /app
ENTRYPOINT ["gunicorn", "main:create_app()", "--config", "gunicorn.conf.py"]