FROM python:3.8.0-slim

# Copy local code to the container image
COPY templates /app/templates
COPY .env /app/.env
COPY main.py /app/main.py
COPY get_relevant_page.py /app/get_relevant_page.py
COPY requirements.txt /app/requirements.txt
COPY function.py /app/function.py
COPY constant.py /app/constant.py

COPY static/ /app/static/
# Sets the working directory
WORKDIR /app

# Upgrade PIP
RUN pip install --upgrade pip

#Install python libraries from requirements.txt
RUN pip3 install -r requirements.txt

# Set $PORT environment variable
ENV PORT 8080
EXPOSE 8080
# Run the web service on container startup