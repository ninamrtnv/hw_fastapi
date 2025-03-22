import uvicorn
from api.app import create_app
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
