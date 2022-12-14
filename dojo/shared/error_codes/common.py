from dojo.shared.error_messages import ErrorMessage


class UnsupportedActionForService(ErrorMessage):
    error_code = "unsp_001"
    error_message = "This action is not supported for this service."


class ServiceMaintainance(ErrorMessage):
    error_code = "serv_001"
    error_message = "This service is currently undergoing maintainance."


class ServiceUnavailable(ErrorMessage):
    error_code = "serv_002"
    error_message = "This service is currently unavailable."


class ServiceLevelError(ErrorMessage):
    error_code: str = "serv_003"
    error_message = (
        "Our service is unable to process your request. Please try again later."
    )


class RestApiMaintenance(ErrorMessage):
    error_code = "rest_001"
    error_message = "This API is currently undergoing maintainance."


class RestApiUnavailable(ErrorMessage):
    error_code = "rest_002"
    error_message = "This API is currently unavailable."


class RestApiDisabled(ErrorMessage):
    error_code: str = "rest_003"
    error_message = "This API is currently disabled."


error_codes = [
    UnsupportedActionForService,
    ServiceMaintainance,
    ServiceUnavailable,
    RestApiMaintenance,
    RestApiUnavailable,
    RestApiDisabled,
    ServiceLevelError,
]
