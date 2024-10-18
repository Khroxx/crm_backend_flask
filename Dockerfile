FROM python:latest

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt 

COPY . /app/

ENV FLASK_APP=run.py
ENV FLASK_ENV=development


EXPOSE 5000

CMD ["python", "/app/run.py"]