FROM python:3-alpine3.22

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
ADD . /app
WORKDIR /app

CMD ["python", "main.py"]