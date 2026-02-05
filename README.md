# BHCLI Impact OS

This repository contains a starter monorepo scaffold for the BHCLI Impact OS described in `docs/PRD.md`. It provides a minimal Next.js frontend, a FastAPI backend with stubbed endpoints, shared packages for design tokens/types, and worker stubs for ingestion/AI/export jobs.

## Structure

```
/apps/web            # Next.js frontend
/apps/api            # FastAPI backend
/packages/ui         # design system tokens
/packages/shared     # shared schemas (future)
/services/worker     # background jobs (Celery/RQ stubs)
/infra               # infrastructure placeholders
```

## Quick start

### Frontend

```bash
cd apps/web
npm install
npm run dev
```

### Backend

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Worker (stub)

```bash
cd services/worker
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Notes

* Endpoints in the API are stubbed with `NotImplemented` responses for now.
* The UI is a skeletal BHCLI-styled landing page; expand with feature pages per PRD.
