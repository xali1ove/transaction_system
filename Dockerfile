FROM python:3.9

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /usr/src/app/
RUN ["chmod", "+x", "build.sh"]
EXPOSE 8000
