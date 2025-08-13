ARG PYTHON_VERSION=3.13.5

FROM python:3.13.5-slim as Build-image

WORKDIR /accelerator

ENV PYTHONDONTWRITEBYTECODE=1 \
    WORKDIR_PATH=WORKDIR \
    VENV_PATH="/venv" \
    PYTHONUNBUFFERED="true"


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install virtual env
RUN python -m venv $VENV_PATH
ENV PATH ="$VENV_PATH/bin:$PATH"

RUN pip install --no-cache-dir --compile --upgrade pip poetry wheel

COPY ./pyproject.toml /accelerator/pyproject.toml
COPY ./poetry.lock /accelerator/poetry.lock

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

COPY ./src /accelerator/src
COPY ./main.py /accelerator/main.py
COPY ./deployments/entrypoint.sh /accelerator/deployments/entrypoint.sh

RUN chmod +x /accelerator/deployments/entrypoint.sh

EXPOSE 9001

CMD ["./deployments/entrypoint.sh"]
