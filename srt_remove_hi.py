#!/usr/bin/env python3

import srt, argparse, os

parser = argparse.ArgumentParser(description="path to srt")
parser.add_argument("srt_files", nargs="+", help="path to srt(s)")
args = parser.parse_args()

print(args.srt_files)
cwd = os.getcwd()

for srt_file in args.srt_files:
    srt_file = os.path.join(cwd, srt_file)
    subtitle_file = srt.srt_file(srt_file)
    subtitle_file.remove_hearing_impaired()
    subtitle_file.save()
