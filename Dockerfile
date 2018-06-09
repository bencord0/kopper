FROM python
RUN pip install pipenv

WORKDIR /app/
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy

COPY . /app/
