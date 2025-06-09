# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose default Streamlit port (if needed)
EXPOSE 8501

# Set entry point for CLI pipeline (can be changed to Streamlit or FastAPI)
CMD ["python", "run_pipeline.py"]
