from pipelines.training import ml_pipeline
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("🚀 Attempting Training Run...")
    try:
        ml_pipeline()
        print("✅ SUCCESS: Training Finished!")
    except Exception as e:
        print(f"❌ FAILED: {e}")
        import traceback
        traceback.print_exc()