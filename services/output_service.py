from pathlib import Path


class OutputService:
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def save_markdown(self, filename: str, content: str) -> Path:
        file_path = self.output_dir / filename
        file_path.write_text(content, encoding="utf-8")
        return file_path