FROM python:3.10.2

ENV POETRY_VERSION=1.1.13
ENV PATH="${PATH}:/root/.local/bin/"

COPY . .

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && poetry install --no-dev
RUN wget https://raw.githubusercontent.com/celsiusnarhwal/github-markdown-css/main/github-css.html
RUN gh-md-to-html README.md -c -x github-css.html

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]