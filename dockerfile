FROM python:latest
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /src
 WORKDIR /src
 ADD requirements.txt /src/
 RUN pip install -r requirements.txt

#Install cron
 RUN apt-get update
 RUN apt-get --yes --no-install-recommends install cron
 RUN apt-get install nano
 
# Add crontab file in the cron directory
 ADD crontab /etc/cron.d/hello-cron
# Give execution rights on the cron job
 RUN chmod 0644 /etc/cron.d/hello-cron
 RUN touch /var/log/cron.log
 ADD . /src/
 RUN chmod '+x' /src/sc.sh 
