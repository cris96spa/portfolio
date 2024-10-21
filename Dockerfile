FROM python:3.12.6

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install curl -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip setuptools wheel \
    && pip install uv

COPY ./pyproject.toml ./pyproject.toml

COPY ./home ./home
COPY ./portfolio ./portfolio
COPY ./staticfiles ./staticfiles
COPY ./static ./static
COPY ./templates ./templates
COPY ./db.sqlite3 ./db.sqlite3 
COPY ./manage.py ./manage.py
RUN uv pip compile pyproject.toml --extra dev -o requirements.txt --extra-index-url https://pypi.org/simple/ --no-cache
RUN pip install -r requirements.txt --extra-index-url https://pypi.org/simple/ --no-cache
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
CMD ["python", "manage.py", "runserver"]
# Run the application using a WSGI server
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]