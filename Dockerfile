FROM python:3.8.7
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY app.py entrypoint.sh VERSION.txt config.toml ./
ENTRYPOINT ["/app/entrypoint.sh"]
