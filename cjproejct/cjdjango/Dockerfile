FROM python:3.8-slim
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && \ 
  pip install -r requirements.txt
COPY . /code 
CMD ["python", "./fc_community/manage.py", "runserver", "0.0.0.0:8000"]