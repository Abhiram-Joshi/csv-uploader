def response_writer(status: str, data: dict, code: int, message: str) -> dict:
    return {
        "status": status,
        "data": data,
        "code": code,
        "message": message,
    }
