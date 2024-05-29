from fastapi import APIRouter, File, UploadFile, BackgroundTasks
from tasks.analysis_tasks import analyze_dataset
from utils.data_validator import validate_csv
from config import celery_app

router = APIRouter()


@router.post("/analyze_dataset")
async def analyze_dataset_endpoint(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    # Validate uploaded file
    is_valid, df_or_error = validate_csv(file.file)
    if not is_valid:
        return {"error": df_or_error}

    # Offload the analysis task to a background worker
    task = analyze_dataset.delay(df_or_error)

    # Return task ID

    return {"task_id": task.id}
