FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r /code/requirements.txt

ENTRYPOINT ["sh", "/code/entrypoint.sh"]