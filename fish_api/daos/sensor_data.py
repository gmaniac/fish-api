from flask import abort

from fish_api.documents.sensor_data import SensorData


class SensorDataDAO:
    @staticmethod
    def get_count(kword):
        return SensorData.objects(**kword).count()

    @staticmethod
    def get_all(sensor: str = None, page: int = 1, count: int = 10):
        sensor_data_query = SensorData.objects(sensor=sensor)
        offset = (page - 1) * count
        return SensorData.objects.skip(offset).limit(count)

    @staticmethod
    def get(kword):
        return SensorData.objects(**kword).first()
    
    @staticmethod
    def create(sensor, value=None, unit=None):
        sensor_data = SensorData(
            sensor=sensor.id,
            value=value,
            unit=unit,
        )

        return sensor_data.save()

    @staticmethod
    def delete(args):
        sensor = SensorData.objects(**args).first()

        if sensor is None:
            abort(404, "Sensor data not found")

        sensor.delete()

        return {'message': "Sensor data removed"}, 201

    @staticmethod
    def update(sensor_data_id, args):
        try:
            sensor_data = SensorData.objects(id=sensor_data_id).first()
            if sensor_data is None:
                abort(404, "Sensor data not found")

            if not args or len(args) < 1:
                abort(411, "Length required")

            sensor_data.update(**args)
            sensor_data.reload()

            return sensor_data
        except Exception as e:
            abort(500, "Failed to update sensor data")

