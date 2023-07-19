# syntax=docker/dockerfile:1
FROM python:3.10-alpine
RUN mkdir /code
WORKDIR /code
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV PORT 5000
EXPOSE 5000
COPY . .

CMD ["flask", "run"]
