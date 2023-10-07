FROM python:3.10.8-slim
LABEL description="Sentiment classifier of tweets service"
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 6000
CMD ["python",  "app.py"]