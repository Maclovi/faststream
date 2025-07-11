from opentelemetry.metrics import Meter, MeterProvider
from opentelemetry.trace import TracerProvider

from faststream.kafka.opentelemetry.provider import (
    telemetry_attributes_provider_factory,
)
from faststream.kafka.response import KafkaPublishCommand
from faststream.opentelemetry.middleware import TelemetryMiddleware


class KafkaTelemetryMiddleware(TelemetryMiddleware[KafkaPublishCommand]):
    def __init__(
        self,
        *,
        tracer_provider: TracerProvider | None = None,
        meter_provider: MeterProvider | None = None,
        meter: Meter | None = None,
    ) -> None:
        super().__init__(
            settings_provider_factory=telemetry_attributes_provider_factory,
            tracer_provider=tracer_provider,
            meter_provider=meter_provider,
            meter=meter,
            include_messages_counters=True,
        )
