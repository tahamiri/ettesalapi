FROM python:latest

RUN mkdir /app

WORKDIR /app

COPY req.txt .

RUN pip install -r req.txt

COPY . .

EXPOSE 8989

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8989"]