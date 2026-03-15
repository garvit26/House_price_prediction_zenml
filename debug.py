import sys
import logging
from pipelines.training import ml_pipeline

# Setup logging to see everything
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    print("--- STARTING DEBUG RUN ---")
    print(f"Python path: {sys.path[0]}")
    
    try:
        print("Executing ml_pipeline()...")
        # Ensure you call the function here!
        run = ml_pipeline()
        print("--- PIPELINE FINISHED SUCCESSFULLY ---")
    except Exception as e:
        print(f"!!! PIPELINE FAILED !!!")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {e}")
        import traceback
        traceback.print_exc()