FROM python:3.12.4-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY development_folder /app/development_folder
COPY src/cleaning_data.py /app/src/cleaning_data.py
COPY config/tfidvectorizer.pkl /app/config/tfidvectorizer.pkl


EXPOSE 8000
CMD ["uvicorn", "development_folder.app:app", "--host", "0.0.0.0", "--port", "8000"]