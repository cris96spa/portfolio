ARG PYTHON_VERSION=3.12-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip setuptools wheel \
    && pip install uv

RUN mkdir -p /code

WORKDIR /app

RUN pip install poetry
COPY ./pyproject.toml ./pyproject.toml
RUN uv pip compile pyproject.toml --extra dev -o requirements.txt --extra-index-url https://pypi.org/simple/ --no-cache
RUN pip install -r requirements.txt --extra-index-url https://pypi.org/simple/ --no-cache
COPY . /app

ENV SECRET_KEY "mMV6vgXTs9qs3flESOrCkA0WDwgO96rWtnoTKqiaRAJug9u5qU"

EXPOSE 8000
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]

