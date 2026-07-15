"""
=========================================================
    Modernized Web Portal for Healthcare (PBM)
    AI-Powered UX

    Main Application Entry Point
=========================================================
"""

import os

from app import create_app


# =========================================================
# Environment
# =========================================================

config_name = os.getenv(

    "FLASK_ENV",

    "development"

)


# =========================================================
# Create Flask App
# =========================================================

app = create_app(config_name)


# =========================================================
# Run Application
# =========================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=app.config["DEBUG"]

    )

    