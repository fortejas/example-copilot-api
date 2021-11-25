FROM public.ecr.aws/docker/library/python:3.9.9

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x start_server.sh

EXPOSE 5000

CMD ["/usr/src/app/start_server.sh"]
