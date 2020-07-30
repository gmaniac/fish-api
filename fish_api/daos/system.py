from flask import abort

from fish_api.documents.system import System


class SystemDAO:
    @staticmethod
    def get(kword):
        return System.objects(**kword).first()

    @staticmethod
    def get_all(page: int = 1, count: int = 10):
        offset = (page - 1) * count
        return System.objects.skip(offset).limit(count)

    @staticmethod
    def create(name=None, description=None):
        system = System(
            name=name,
            description=description
        )

        return system.save()

    @staticmethod
    def delete(args):
        if len(args) < 1:
            abort(411, "Length required")

        for arg in args:
            system = System.objects(**arg).first()

            if system is None:
                continue

            system.delete()

        return {'message': "system(s) removed"}, 201

    @staticmethod
    def update(system_id, args):
        try:
            system = System.objects(id=system_id).first()
            if system is None:
                abort(404, "System not found")

            if not args:
                abort(411, "Length required")

            system.update(**args)
            system.reload()

            return system
        except Exception as e:
            abort(500, "Failed to create user")

