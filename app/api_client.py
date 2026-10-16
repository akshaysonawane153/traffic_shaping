import requests

class TrafficAPIClient:
    def __init__(self, baseurl):
        self.base_url = baseurl
        self.session = requests.Session()

    def get_records(self):
        print(self.base_url + "/api/get_all_records")
        return self.session.get(self.base_url + "/api/get_all_records", timeout=5)

    def get_health_status(self):
        return self.session.get(self.base_url + "/api/health_status", timeout=5)

    def get_total_records(self):
        return self.session.get(self.base_url + "/api/total_records", timeout=5)

    def close_session(self):
        return self.session.close()
