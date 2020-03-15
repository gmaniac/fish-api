from pets_api.papi.documents.tokens import Token


class TokenDAO:
    @staticmethod
    def get(kword):
        return Token.objects(**kword).first()

