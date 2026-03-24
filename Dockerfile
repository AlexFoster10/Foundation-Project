FROM demisto/fastapi:0.125.0.7704170

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "app/src/main.py"]





