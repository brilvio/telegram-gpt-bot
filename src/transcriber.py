import whisper

from .settings import settings

model = whisper.load_model(
    settings.whisper_model,
    device=settings.whisper_device,
)


def transcribe(file):
    return whisper.transcribe(
        model, file, language=settings.whisper_language, verbose=True
    )
