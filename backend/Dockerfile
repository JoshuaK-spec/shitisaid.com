## This dockerimage builds the backend container used
## to run shitisaid.com, a free online transcripts amalgamator. 

### ===============================
### ===============================
### ===============================

## Base Python Image (Slim - Saves a lot of space and reduces attack vectors)
FROM python:3.14-slim

# Permanent default work directory. The project directory itself.
WORKDIR /usr/local/shitisaid/

# Install dependencies first so this layer is cached between code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container.
COPY . .

RUN useradd --no-create-home backend_runner
USER backend_runner

EXPOSE 8000

CMD ["gunicorn", "main:app", "--workers", "4", "--bind", "0.0.0.0:8000"]



### =================== REFERENCES ===================
# https://docs.docker.com/guides/python/containerize/
# https://docs.gunicorn.org/en/stable/run.html

### =================== AUTHOR ===================
# Luke Mitchell, 2026
