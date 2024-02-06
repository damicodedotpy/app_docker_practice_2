FROM ubuntu

WORKDIR /app

RUN apt-get update
RUN apt-get install python3 -y python3-pip -y

COPY app.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
