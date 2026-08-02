from __future__ import annotations

import logging
import os

from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)
    _configure_logging(app)

    @app.get("/")
    def index() -> str:
        return render_template("index.html")

    @app.get("/health")
    def health() -> str:
        return "ok", 200

    return app


def _configure_logging(app: Flask) -> None:
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    app.logger.setLevel(level)


app = create_app()


if __name__ == "__main__":
    port = int(os.getenv("PORT", os.getenv("FLASK_PORT", "5000")))
    app.run(
        host=os.getenv("FLASK_HOST", "0.0.0.0"),
        port=port,
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
    )