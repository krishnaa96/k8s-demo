FROM python:3.7-slim

WORKDIR /app

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pip3 install flask && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

COPY webapp.py ./

CMD ["python", "webapp.py"]
