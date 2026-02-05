from fastapi import APIRouter

from app.core.responses import not_implemented

router = APIRouter()


@router.post("/reports")
def create_report():
    return not_implemented("Report creation is not implemented.")


@router.get("/reports/{report_id}")
def get_report(report_id: str):
    return not_implemented(f"Report retrieval for {report_id} is not implemented.")


@router.put("/reports/{report_id}")
def update_report(report_id: str):
    return not_implemented(f"Report update for {report_id} is not implemented.")


@router.post("/reports/{report_id}/generate_section")
def generate_report_section(report_id: str):
    return not_implemented(f"Report section generation for {report_id} is not implemented.")


@router.post("/reports/{report_id}/export")
def export_report(report_id: str):
    return not_implemented(f"Report export for {report_id} is not implemented.")


@router.get("/exports/{export_id}")
def get_export(export_id: str):
    return not_implemented(f"Export retrieval for {export_id} is not implemented.")
