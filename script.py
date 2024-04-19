import sys

from datetime import datetime
from pathlib import Path

from google.protobuf.json_format import MessageToJson

from tachi.tachi_pb2 import Backup

def main(input_file: Path, output_file: Path|None = None):
    output_file = output_file or Path('./backup.json')
    
    with input_file.open('rb') as f:
        raw_data = f.read()
    if raw_data[:2] == b'\x1f\x8b':
        import gzip
        data = gzip.decompress(raw_data)
    else:
        data = raw_data
    
    backup = Backup()
    backup.ParseFromString(data)
    output_file.write_text(MessageToJson(backup))

def cli():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input-file')
    parser.add_argument('-o','--output-file')
    args = parser.parse_args()

    input_file = Path(args.input_file)
    output_file = Path(args.output_file) if args.output_file else Path('backup.json')
    now = datetime.now().strftime("%Y-%jT%H%M%S")
    if not input_file.exists():
        print(f'file {input_file=} not found; exiting', file=sys.stderr)
        raise SystemExit(1)
    if not input_file.is_file():
        print(f'file {input_file=} not a file; exiting', file=sys.stderr)
        raise SystemExit(1)
    if output_file.exists():
        print(f'file {output_file=} exists; appending `-{now}` to end', file=sys.stderr)
        output_file = output_file.with_stem(f"{output_file.stem}-{now}")

    main(input_file, output_file)


if __name__ == "__main__":
    cli()
