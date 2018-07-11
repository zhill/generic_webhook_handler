FROM alpine

COPY . /app
WORKDIR /app
RUN apk update ; apk add python py-pip
RUN pip install --upgrade pip ; pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
