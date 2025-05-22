FROM python:3.7

RUN mkdir /wd
COPY /app/  /wd/
WORKDIR /wd
RUN pip install -r requirements.txT

EXPOSE 5000
CMD ["python", "main.py"]
