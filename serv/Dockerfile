FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python3 -m pip install --upgrade pip && pip install pipenv

COPY . /app/
#python -m pip install --upgrade pip &&
#--dev --system --deploy
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pipenv install --system --deploy --ignore-pipfile
#разкомментить если хуйня выше не шпилит
#RUN pipenv lock && pipenv requirements > requirements.txt && python3 -m pip install -r requirements.txt
#    cd .. && apk --purge del .build-deps

#RUN apt-get -y update \
#    && apt-get -y install postgresql-dev gcc python3-dev musl-dev
#RUN pip3 install pipenv && pipenv install --system --deploy --ignore-pipfile

#RUN pipenv lock && pipenv install --dev --system

#RUN pip install pipenv && pipenv install --dev --system --deploy

#CMD ['python', '/autoshop1/manage.py', 'runserver', '0.0.0.0:8000']
#ADD docker-entrypoint.sh /docker-entrypoint.sh
#RUN chmod a+rxw docker-entrypoint.sh
#ENTRYPOINT docker-entrypoint.sh