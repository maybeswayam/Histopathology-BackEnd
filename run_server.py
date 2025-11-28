#!/usr/bin/env python3
"""
Production-safe script to run the FastAPI server on Railway
"""

import uvicorn
import os
import sys

def main():
    """Run the FastAPI server"""

    # Create model directory if missing
    if not os.path.exists("models"):
        print("Creating models directory...")
        os.makedirs("models")

    # Check for model file
    model_files = ["models/best_model.pth", "models/model_best.pth"]
    model_found = any(os.path.exists(path) for path in model_files)

    if not model_found:
        print("Warning: No model file found. Looking for either:")
        for path in model_files:
            print(f"- {path}")
        print("\nServer will still start.")

    # Railway dynamic PORT
    port = int(os.getenv("PORT", 8000))

    print("Starting Histopathology Cancer Detection API server...")
    print(f"Server running on port: {port}")
    print("API docs: /docs")

    try:
        uvicorn.run(
            "app:app",
            host="0.0.0.0",
            port=port,
            reload=False,   # IMPORTANT
            log_level="info"
        )
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
