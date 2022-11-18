FROM python:3.9.12


COPY ./requirements.txt /app/
COPY ./main.py /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]