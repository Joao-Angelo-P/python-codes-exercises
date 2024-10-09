# Melhorando leitura de arquivos
from pathlib import Path

def __load__file(filepath: Path | str) -> list[str]:
	with open(filepath, 'r') as f:
		return [x.strip() for x in f if x != '/n']
