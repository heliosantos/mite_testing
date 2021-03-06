from mite.exceptions import MiteError


def check_status_code(resp, expectedStatusCode):
    """Raise an MiteError if the response has an unexpected status code.

    Args:
        resp: the response to falidate
        expectedStatusCode: the status code expected the response to have

    NOTE:
    There's a call to this function on the scripts created using the HAR converter.
    The source code to the funcion in not part of the scripts and is not in the mite repo.
    I'm not sure if this is the best approach but failed requests will return a MiteError since the contex handles it differently than other expections.
    """
    if resp.status_code != expectedStatusCode:
        raise MiteError(f"Invalid status code. Expected: {expectedStatusCode}, Actual: {resp.status_code} ")


def check_text(resp, needle):
    """Raise an error if the response doesn't contain the given string.

    Args:
        needle: the text to find in the response

    """

    if needle not in resp.text:
        raise MiteError(f"Couldn't find \"{needle}\" in the response.")
