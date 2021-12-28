from requests import get
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    ip = get('https://api.ipify.org').text
    return func.HttpResponse(f"IP address as seen by ipify.org:, {ip}.")