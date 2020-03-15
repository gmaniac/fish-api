from pets_api.documents.tokens import Token


class TokenDAO:
    @staticmethod
    def get(kword):
        return Token.objects(**kword).first()

