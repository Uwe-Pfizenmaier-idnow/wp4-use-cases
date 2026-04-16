#!/usr/bin/env python3

import json
import os
import re
import shutil
import subprocess
from collections import defaultdict

from natsort import natsorted

md_inputs = natsorted([f for f in os.listdir(".") if f.endswith(".md")])


def set_nested(d: dict, keys: list, value):
    assert len(keys) > 0
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value


def gather_inputs(d: dict) -> list:
    if "input" not in d:
        return []
    ret = [d["input"]]
    for v in d.values():
        if "input" in v:
            for input in gather_inputs(v):
                ret += [input]
    return ret


def generate_qmd(md: str) -> str:
    with open(md, "r") as md_file:
        lines = [line for line in md_file]
    qmd = md.replace(".md", ".qmd")
    # Add section anchor
    if len(lines) > 0 and lines[0].startswith("#"):
        sec_anchor = "sec-" + qmd.split("--")[0].replace(".", "_")
        lines[0] = lines[0][:-1] + " {#" + sec_anchor + "}" + "\n"
    with open(qmd, "w") as qmd_file:
        for line in lines:
            # Fix Mermaid syntax for Quarto
            line = line.replace('```mermaid', '```{mermaid}')
            qmd_file.write(line)
    return qmd


def main():
    # Detect section/annex structure
    sections = defaultdict(dict)
    section_prefix = re.compile("[1-9](\\.[0-9]*)*--")
    annexes = defaultdict(dict)
    for md in md_inputs:
        if section_prefix.match(md):
            print(f"Found section: {md}")
            qmd = generate_qmd(md)
            section_number_path = md.split("--")[0].split(".")
            set_nested(sections, section_number_path, {"input": qmd})
        elif md.startswith("Annex-"):
            print(f"Found annex: {md}")
            qmd = md.replace(".md", ".qmd")
            shutil.copyfile(md, qmd)
            annex_number_path = md[len("Annex-"):].split("--")[0].split(".")
            set_nested(annexes, annex_number_path, {"input": qmd})
        else:
            print(f"Ignoring Markdown file: {md}")

    # Generate section/annex Quarto files
    for top_level_section in list(sections.values()) + list(annexes.values()):
        qmd_file = top_level_section["input"]
        print(f"Processing {qmd_file}...")
        with open(qmd_file, "a") as f:
            for subsection in top_level_section.values():
                for input in gather_inputs(subsection):
                    f.write("{{< include " + input + " >}}\n")

    for first_top_level_section in sections.values():
        qmd_file = first_top_level_section["input"]
        shutil.copy(qmd_file, "index.qmd")
        break

    # print(json.dumps(sections, indent=4))

    subprocess.run(["quarto", "render", "--to", "html"])
    subprocess.run(["quarto", "render", "--no-clean", "--to", "pdf"])
    subprocess.run(["quarto", "render", "--no-clean", "--to", "docx"])


if __name__ == "__main__":
    main()
