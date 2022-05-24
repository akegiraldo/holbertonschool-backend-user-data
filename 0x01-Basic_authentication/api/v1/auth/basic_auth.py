from api.v1.auth.auth import Auth


class BasicAuth(Auth):

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        prefix = 'Basic '
        if not authorization_header or not isinstance(authorization_header, str) or not \
                authorization_header.startswith(prefix):
            return None

        return authorization_header.replace(prefix, '')
