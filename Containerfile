FROM python:3.13-slim

RUN python -m venv /venv
ENV PATH="/venv/bin/:$PATH"

RUN pip install "django<6" gunicorn whitenoise

COPY src /src
WORKDIR /src

RUN python manage.py collectstatic
ENV DJANGO_DEBUG_FALSE=1

RUN adduser --uid 1234 nonroot
USER nonroot

CMD ["gunicorn", "--bind", ":8888", "superlists.wsgi:application"]

