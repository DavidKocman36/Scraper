FROM python:3.11-alpine
ENV FLASK_APP=app.py

WORKDIR /src

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]