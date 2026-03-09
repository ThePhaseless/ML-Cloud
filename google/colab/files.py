"""Local replacement for google.colab.files that works outside of Colab."""

from pathlib import Path


def upload(*file_paths: str) -> dict[str, bytes]:
    """Mimic google.colab.files.upload() by reading local files.

    Args:
        *file_paths: Paths to files to load. If none provided, prompts user for input.

    Returns:
        Dict mapping filename to file bytes content.
    """
    if not file_paths:
        raw = input("Podaj ścieżki do plików (oddzielone przecinkiem): ")
        file_paths = tuple(p.strip() for p in raw.split(",") if p.strip())

    uploaded = {}
    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            print(f"Plik nie istnieje: {file_path}")
            continue
        uploaded[path.name] = path.read_bytes()
        print(f"Załadowano '{path.name}' ({len(uploaded[path.name])} bajtów)")

    return uploaded
