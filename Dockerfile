FROM python:3.10-buster
WORKDIR /workdir

ENV POETRY_HOME /opt/poetry
ENV PATH $PATH:$POETRY_HOME/bin
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN poetry config virtualenvs.create false
