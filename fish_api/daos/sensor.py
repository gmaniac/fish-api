from flask import abort

from fish_api.documents.sensor import Sensor


class SensorDAO:
    @staticmethod
    def get_count(kword):
        return Sensor.objects(**kword).count()

    @staticmethod
    def get_all(page: int = 1, count: int = 10):
        offset = (page - 1) * count
        return Sensor.objects.skip(offset).limit(count)

    @staticmethod
    def get(kword):
        return Sensor.objects(**kword).first()

    @staticmethod
    def create(system, name=None, sensor_type=None, description=None):
        sensor = Sensor(
            system=system.id,
            name=name,
            type=sensor_type,
            description=description
        )

        return sensor.save()

    @staticmethod
    def delete(args):
        if len(args) < 1:
            abort(411, "Length required")

        for arg in args:
            sensor = Sensor.objects(**arg).first()

            if sensor is None:
                continue

            sensor.delete()

        return {'message': "Sensor(s) removed"}, 201

    @staticmethod
    def update(sensor_id, args):
        try:
            sensor = Sensor.objects(id=sensor_id).first()
            if sensor is None:
                abort(404, "Sensor not found")

            if not args or len(args) < 1:
                abort(411, "Length required")

            sensor.update(**args)
            sensor.reload()

            return sensor
        except Exception as e:
            abort(500, "Failed to update sensor")

