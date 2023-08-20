FROM alpine:latest

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python \
&& python3 -m ensurepip \
&& pip3 install --no-cache --upgrade pip Flask pymongo gunicorn

COPY app.py /app/app.py

EXPOSE 4433

CMD ["gunicorn", "--bind", "0.0.0.0:4433", "app:app"]
