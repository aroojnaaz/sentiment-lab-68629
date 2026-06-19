# Sentiment Lab

Minimal sentiment analysis project scaffold for experimentation.

## Structure

- data/
  - raw/
  - processed/
- notebooks/
- src/
- results/
- mlruns/

## Setup

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

- Place raw data in `data/raw`.
- Use `notebooks/` for experiments and `src/` for reusable code.
- MLflow runs are stored in `mlruns/`.

## Config

Project configuration is in `config.json`.
