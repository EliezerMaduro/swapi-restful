from celery import shared_task
from apps.ingestion.utils import fetch_swapi_data, save_deltas
import logging

logger = logging.getLogger(__name__)

@shared_task
def run_swapi_ingestion():
    logger.info("Starting SWAPI ingestion task")
    try:
        data = fetch_swapi_data()
        save_deltas(data)
        logger.info("SWAPI ingestion task completed successfully")
    except Exception as e:
        logger.error(f"Error in SWAPI ingestion task: {e}")
        raise