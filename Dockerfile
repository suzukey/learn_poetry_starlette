FROM python:3.8-slim as builder

WORKDIR /build
RUN pip install poetry

COPY learn/* ./learn/
COPY poetry.lock pyproject.toml /build/

RUN poetry build

# ------------------

FROM python:3.8-slim
WORKDIR /app
COPY --from=builder /build/dist/learn-*-py3-none-any.whl .
RUN pip install learn-*-py3-none-any.whl

CMD ["uvicorn", "learn.main:app", "--host", "0.0.0.0", "--port", "80"]
