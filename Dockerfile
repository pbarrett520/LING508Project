FROM python:3.11

EXPOSE 5001

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

#CMD tail -f /dev/null
CMD python app.py