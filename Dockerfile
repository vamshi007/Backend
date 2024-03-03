FROM python:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY req.txt .

RUN pip install --upgrade pip && pip install -r req.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

