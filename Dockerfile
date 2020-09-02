FROM python:3.8-slim

WORKDIR /app
RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install

COPY learn/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
