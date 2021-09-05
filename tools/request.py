import copy
import requests
class RequestType:
    get='get'
    post='post'
    delete='delete'
    put='put'

class Request:
    headers = {
        'LANG': 'cn',
        'Content-Type': 'application/json',
    }
    timeout = 10

    def get_response(self, url, test_params, test_headers, request_type, expect_return_code):
        headers = copy.deepcopy(self.headers)
        headers.update(test_headers or {})
        response = self.__send_request(request_type, url, headers, test_params)
        if response.status_code == expect_return_code:
            return response
        raise Exception("Response error, status code {}, error info: {}".format(response.status_code, response.content))

    def get_json(self, url, test_params=None, test_headers=None, request_type=RequestType.post, expect_return_code=200):
        return self.get_response(url, test_params, test_headers, request_type, expect_return_code).json()

    def get_text(self, url, test_params=None, test_headers=None, request_type=RequestType.post, expect_return_code=200):
        return self.get_response(url, test_params, test_headers, request_type, expect_return_code).text

    def get_headers(
            self, url, test_params=None, test_headers=None, request_type=RequestType.post, expect_return_code=200):
        return self.get_response(url, test_params, test_headers, request_type, expect_return_code).headers

    @staticmethod
    def __send_request(request_type, url, headers, test_params, allow_redirects=True):
        test_params = {} if request_type == RequestType.get else test_params
        return requests.request(
            request_type, url, headers=headers, json=test_params, verify=False, allow_redirects=allow_redirects)
