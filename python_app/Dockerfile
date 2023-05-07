FROM python:3.9

RUN pip install mysql-connector-python
RUN pip install flask

COPY . ./

CMD ["python3", "app_web.py"]

EXPOSE 5000
