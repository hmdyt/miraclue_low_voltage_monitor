FROM python:3.10-buster
WORKDIR /workdir

ENV POETRY_HOME /opt/poetry
ENV PATH $PATH:$POETRY_HOME/bin
RUN curl -sSL https://install.python-poetry.org | python -
RUN poetry config virtualenvs.create false

COPY ./miraclue_low_voltage_monitor /workdir/miraclue_low_voltage_monitor
COPY ./pyproject.toml /workdir/pyproject.toml
COPY ./poetry.lock /workdir/poetry.lock

RUN poetry install