from opentelemetry.metrics import Meter, MeterProvider
from opentelemetry.trace import TracerProvider

from faststream.opentelemetry.middleware import TelemetryMiddleware
from faststream.redis.opentelemetry.provider import RedisTelemetrySettingsProvider
from faststream.redis.response import RedisPublishCommand


class RedisTelemetryMiddleware(TelemetryMiddleware[RedisPublishCommand]):
    def __init__(
        self,
        *,
        tracer_provider: TracerProvider | None = None,
        meter_provider: MeterProvider | None = None,
        meter: Meter | None = None,
    ) -> None:
        super().__init__(
            settings_provider_factory=lambda _: RedisTelemetrySettingsProvider(),
            tracer_provider=tracer_provider,
            meter_provider=meter_provider,
            meter=meter,
            include_messages_counters=True,
        )
