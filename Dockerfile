FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./news ./news
COPY ./factory.py ./factory.py
COPY ./main.py ./main.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]