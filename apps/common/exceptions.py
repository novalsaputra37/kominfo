from rest_framework.views import exception_handler


def common_exception_handler(exc, context):
    response = exception_handler(exc, context)

    handlers = {
        "NotFound": _handle_not_found_error,
        "ValidationError": _handle_generic_error,
        "PermissionDenied": _handle_permission_denied,
        # "ParseError": _handle_generic_error,
        "Http404": _handle_generic_error,
    }

    exception_class = exc.__class__.__name__
    print("exception_handler", exception_class)

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def _handle_generic_error(exc, context, response):
    response.data = {
        "success": False,
        "message": "incorrect data",
        "data": response.data,
    }
    return response


def _handle_permission_denied(exc, context, response):
    response.data = {
        "success": False,
        "message": "not have permission",
        "data": response.data,
    }
    return response


def _handle_not_found_error(exc, context, response):
    view = context.get("view", None)

    if view and hasattr(view, "queryset") and view.queryset is not None:
        error_key = view.queryset.model._meta.verbose_name
        response.data = {
            "success": False,
            "message": "not found error",
            "data": {error_key: response.data["detail"]},
        }

    else:
        response = _handle_generic_error(exc, context, response)
    return response
