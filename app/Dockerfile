FROM python:alpine3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV NAME=""
EXPOSE 80
ENTRYPOINT ["python", "./index.py"]
