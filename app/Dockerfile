FROM python:3.7

RUN mkdir /wd
COPY /app/  /wd/
WORKDIR /wd
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "main.py"]
