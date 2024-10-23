FROM ghcr.io/osgeo/gdal:alpine-small-latest

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv

RUN apk add --no-cache python3 py3-pip postgresql-client geos build-base
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN pip install -r /app/requirements.txt

#CMD ["python", "/app/geodjango/manage.py", "runserver", "0.0.0.0:8001"]