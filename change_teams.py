from mitmproxy import http


class ChangeTeam:

    def __init__(self):
            self.modify_request = False

    # mitmproxy event
    def response(self, flow: http.HTTPFlow) -> None:
        if self.request_match(flow) and self.modify_request:
            modified_response = open("./responses/long_name_teams.json", "r").read()
            flow.response.text = modified_response
            print("Change teams responses")

    def request_match(self, flow: http.HTTPFlow) -> bool:
        request_path = flow.request.path
        request_query = flow.request.query
        return "lookup_all_teams" in request_path and request_query["id"] == "4328"

addons = [
    ChangeTeam()
]