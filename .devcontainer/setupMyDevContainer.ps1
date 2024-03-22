try {
    python -m venv .venv
}
catch {}

.\.venv\Scripts\Activate.ps1

poetry install