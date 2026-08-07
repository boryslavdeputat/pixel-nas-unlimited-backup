#!/usr/bin/env python3
"""Estimate how many upload cycles to drain a NAS library through a phone buffer."""
from __future__ import annotations
import argparse, math

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--library-gb", type=float, required=True)
    p.add_argument("--buffer-gb", type=float, default=20)
    p.add_argument("--upload-gb-per-day", type=float, default=15)
    args = p.parse_args()
    cycles = math.ceil(args.library_gb / args.buffer_gb)
    days = args.library_gb / max(args.upload_gb_per_day, 0.1)
    print(f"buffer_cycles_approx={cycles}")
    print(f"calendar_days_approx={days:.1f}")
    print("Limited by the slower of: NAS->phone copy vs Photos upload bandwidth.")

if __name__ == "__main__":
    main()
