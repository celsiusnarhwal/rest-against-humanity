FROM python:3.10.2

ENV POETRY_VERSION=1.1.13
ENV PATH="${PATH}:/root/.local/bin/"

COPY . .

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && poetry install --no-dev

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]