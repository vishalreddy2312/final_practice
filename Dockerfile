FROM python:3.7-alpine3.10

COPY . /final_practice

WORKDIR /final_practice

RUN pip3 install -r requirements.txt

CMD ["pytest"]
