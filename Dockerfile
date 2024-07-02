FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD python src/run.py