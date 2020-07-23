FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD ["python", "-u", "app.py"]