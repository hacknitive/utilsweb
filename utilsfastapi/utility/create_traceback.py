from fastapi import Request


async def create_traceback(
        exc: BaseException,
        request: Request,
        traceback_: str,
) -> str:
    status_code = getattr(exc, "status_code", None)
    code = getattr(exc, "code", None)
    status_code = status_code if status_code else code

    success = getattr(exc, "success", None)
    data = getattr(exc, "data", None)
    error = getattr(exc, "error", None)

    # request_body = str(await request.body())
    request_cookies = str(request.cookies)
    request_headers = str(dict(request.headers))
    request_method = str(request.method)
    request_path_params = str(request.path_params)
    request_query_params = str(request.query_params)
    request_url = str(request.url)

    return str({
        "exc_status_code": status_code,
        "exc_success": success,
        "exc_data": data,
        "exc_error": error,
        # "request_body": request_body,
        "request_cookies": request_cookies,
        "request_headers": request_headers,
        "request_method": request_method,
        "request_path_params": request_path_params,
        "request_query_params": request_query_params,
        "request_url": request_url,
        "traceback": traceback_ or "",
    }
    )
