#!/usr/bin/env python3
"""Check all markdown files for violations of the five tenets."""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import List
from enum import Enum


class Severity(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    NOTE = "NOTE"


class Tenet(Enum):
    DUALISM = "Dualism"
    MINIMAL_QUANTUM = "Minimal Quantum Interaction"
    BIDIRECTIONAL = "Bidirectional Interaction"
    NO_MWI = "No Many Worlds"
    OCCAM_LIMITS = "Occam's Razor Has Limits"


@dataclass
class Violation:
    file_path: str
    tenet: Tenet
    severity: Severity
    description: str
    quote: str
    recommendation: str


def check_dualism_violations(content: str, file_path: str) -> List[Violation]:
    """Check for violations of the Dualism tenet."""
    violations = []

    # ERROR: Endorsing eliminative materialism or reductive physicalism
    patterns_error = [
        (r"consciousness is\s+(merely|just|only|nothing but)\s+(brain|neural|physical)",
         "Claims consciousness is merely physical"),
        (r"consciousness\s+is\s+an?\s+illusion",
         "Claims consciousness is illusory"),
        (r"qualia\s+(do\s+not|don't)\s+exist",
         "Denies existence of qualia"),
        (r"eliminative\s+materialism\s+is\s+(correct|right|true)",
         "Endorses eliminative materialism"),
        (r"consciousness\s+can\s+be\s+fully\s+explained\s+by\s+physics",
         "Claims full physical explanation of consciousness"),
        (r"consciousness\s+reduces\s+to\s+physical",
         "Claims consciousness reduces to physical"),
        (r"purely\s+epiphenomenal",
         "Claims consciousness is purely epiphenomenal"),
    ]

    for pattern, desc in patterns_error:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            context = get_context(content, match.start(), match.end())
            violations.append(Violation(
                file_path=file_path,
                tenet=Tenet.DUALISM,
                severity=Severity.ERROR,
                description=desc,
                quote=context,
                recommendation="Remove or reframe to acknowledge the irreducibility of consciousness"
            ))

    # WARNING: Assuming physicalism without acknowledgment
    patterns_warning = [
        (r"the\s+brain\s+generates\s+consciousness",
         "Assumes brain generates consciousness without qualification"),
        (r"consciousness\s+emerges\s+from\s+complexity",
         "Assumes emergence without addressing hard problem"),
    ]

    for pattern, desc in patterns_warning:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            # Check if there's nearby acknowledgment of the assumption
            context_large = content[max(0, match.start()-500):min(len(content), match.end()+500)]
            if not re.search(r"(assume|if|hypothetically|from\s+a\s+physicalist|materialist\s+view)",
                           context_large, re.IGNORECASE):
                context = get_context(content, match.start(), match.end())
                violations.append(Violation(
                    file_path=file_path,
                    tenet=Tenet.DUALISM,
                    severity=Severity.WARNING,
                    description=desc,
                    quote=context,
                    recommendation="Add qualification acknowledging this assumes physicalism"
                ))

    return violations


def check_quantum_violations(content: str, file_path: str) -> List[Violation]:
    """Check for violations of Minimal Quantum Interaction tenet."""
    violations = []

    # ERROR: Endorsing quantum mysticism
    patterns_error = [
        (r"quantum\s+(healing|mysticism|magic)",
         "Endorses quantum mysticism"),
        (r"consciousness\s+creates\s+reality",
         "Claims consciousness creates reality (quantum woo)"),
        (r"thoughts\s+control\s+quantum",
         "Claims thoughts control quantum outcomes beyond minimal interaction"),
    ]

    for pattern, desc in patterns_error:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            # Check if it's being critiqued rather than endorsed
            context_large = content[max(0, match.start()-200):min(len(content), match.end()+200)]
            if not re.search(r"(reject|dismiss|pseudoscience|not|criticized|false)",
                           context_large, re.IGNORECASE):
                context = get_context(content, match.start(), match.end())
                violations.append(Violation(
                    file_path=file_path,
                    tenet=Tenet.MINIMAL_QUANTUM,
                    severity=Severity.ERROR,
                    description=desc,
                    quote=context,
                    recommendation="Remove or clearly critique quantum mysticism claims"
                ))

    return violations


def check_bidirectional_violations(content: str, file_path: str) -> List[Violation]:
    """Check for violations of Bidirectional Interaction tenet."""
    violations = []

    # ERROR: Endorsing pure epiphenomenalism
    patterns_error = [
        (r"consciousness\s+(has\s+no|cannot\s+have|lacks)\s+causal\s+(power|efficacy|influence)",
         "Claims consciousness has no causal power"),
        (r"epiphenomenalism\s+is\s+(correct|true|right)",
         "Endorses epiphenomenalism"),
        (r"consciousness\s+is\s+causally\s+inert",
         "Claims consciousness is causally inert"),
    ]

    for pattern, desc in patterns_error:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            context = get_context(content, match.start(), match.end())
            violations.append(Violation(
                file_path=file_path,
                tenet=Tenet.BIDIRECTIONAL,
                severity=Severity.ERROR,
                description=desc,
                quote=context,
                recommendation="Remove or reframe to acknowledge consciousness has causal efficacy"
            ))

    return violations


def check_mwi_violations(content: str, file_path: str) -> List[Violation]:
    """Check for violations of No Many Worlds tenet."""
    violations = []

    # ERROR: Endorsing MWI as correct
    patterns_error = [
        (r"many[- ]worlds?\s+(is|interpretation)\s+(correct|true|right)",
         "Endorses many-worlds as correct"),
        (r"all\s+quantum\s+branches\s+are\s+equally\s+real",
         "Endorses MWI ontology"),
        (r"universes?\s+split",
         "Describes universe splitting as fact"),
    ]

    for pattern, desc in patterns_error:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            # Check if it's being discussed rather than endorsed
            context_large = content[max(0, match.start()-200):min(len(content), match.end()+200)]
            if not re.search(r"(if|hypothetically|according\s+to|proponents|reject|dismiss)",
                           context_large, re.IGNORECASE):
                context = get_context(content, match.start(), match.end())
                violations.append(Violation(
                    file_path=file_path,
                    tenet=Tenet.NO_MWI,
                    severity=Severity.ERROR,
                    description=desc,
                    quote=context,
                    recommendation="Clarify that MWI is rejected or qualify as hypothetical"
                ))

    # NOTE: Discussing MWI without noting tenet conflict
    if re.search(r"many[- ]worlds?", content, re.IGNORECASE):
        # Check if there's any mention of rejection or problems
        if not re.search(r"(reject|dismiss|problem|indexical|ontological\s+proliferation)",
                       content, re.IGNORECASE):
            violations.append(Violation(
                file_path=file_path,
                tenet=Tenet.NO_MWI,
                severity=Severity.NOTE,
                description="Discusses MWI without noting rejection",
                quote="[Multiple MWI references without critique]",
                recommendation="Add note that Map rejects MWI per tenets"
            ))

    return violations


def check_occam_violations(content: str, file_path: str) -> List[Violation]:
    """Check for violations of Occam's Razor Has Limits tenet."""
    violations = []

    # ERROR: Using Occam's Razor to dismiss dualism decisively
    patterns_error = [
        (r"dualism\s+(violates|fails)\s+occam",
         "Uses Occam's Razor against dualism"),
        (r"physicalism\s+is\s+simpler,?\s+(therefore|so)\s+(true|correct)",
         "Uses simplicity to argue for physicalism"),
        (r"we\s+should\s+prefer\s+materialism\s+because\s+it'?s\s+simpler",
         "Uses simplicity as decisive argument"),
    ]

    for pattern, desc in patterns_error:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            context = get_context(content, match.start(), match.end())
            violations.append(Violation(
                file_path=file_path,
                tenet=Tenet.OCCAM_LIMITS,
                severity=Severity.ERROR,
                description=desc,
                quote=context,
                recommendation="Remove or acknowledge Occam's Razor is not decisive"
            ))

    return violations


def get_context(content: str, start: int, end: int, window: int = 150) -> str:
    """Extract context around a match."""
    context_start = max(0, start - window)
    context_end = min(len(content), end + window)
    context = content[context_start:context_end].strip()

    # Clean up and truncate
    context = re.sub(r'\s+', ' ', context)
    if len(context) > 300:
        context = context[:297] + "..."

    return context


def check_file(file_path: Path) -> List[Violation]:
    """Check a single file for tenet violations."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

    violations = []
    file_path_str = str(file_path)

    violations.extend(check_dualism_violations(content, file_path_str))
    violations.extend(check_quantum_violations(content, file_path_str))
    violations.extend(check_bidirectional_violations(content, file_path_str))
    violations.extend(check_mwi_violations(content, file_path_str))
    violations.extend(check_occam_violations(content, file_path_str))

    return violations


def main():
    base_path = Path("/home/andy/unfin/unfinishablemap/obsidian")
    topics_path = base_path / "topics"
    concepts_path = base_path / "concepts"

    all_violations = []
    files_checked = []

    # Check all files
    for directory in [topics_path, concepts_path]:
        for file_path in directory.glob("*.md"):
            files_checked.append(file_path)
            violations = check_file(file_path)
            all_violations.extend(violations)

    # Generate report
    print("=" * 80)
    print("TENET VIOLATION ANALYSIS REPORT")
    print("=" * 80)
    print()

    # Summary counts
    errors = [v for v in all_violations if v.severity == Severity.ERROR]
    warnings = [v for v in all_violations if v.severity == Severity.WARNING]
    notes = [v for v in all_violations if v.severity == Severity.NOTE]

    print(f"Files checked: {len(files_checked)}")
    print(f"Total violations found: {len(all_violations)}")
    print(f"  - ERRORS (direct contradictions): {len(errors)}")
    print(f"  - WARNINGS (implicit conflicts): {len(warnings)}")
    print(f"  - NOTES (tensions needing clarification): {len(notes)}")
    print()

    # Group violations by file
    violations_by_file = {}
    for v in all_violations:
        if v.file_path not in violations_by_file:
            violations_by_file[v.file_path] = []
        violations_by_file[v.file_path].append(v)

    # Report violations
    if all_violations:
        print("=" * 80)
        print("VIOLATIONS BY FILE")
        print("=" * 80)
        print()

        for file_path in sorted(violations_by_file.keys()):
            file_violations = violations_by_file[file_path]
            print(f"\n{Path(file_path).name}")
            print("-" * 80)

            for v in file_violations:
                print(f"\n[{v.severity.value}] {v.tenet.value}")
                print(f"Issue: {v.description}")
                print(f"Quote: \"{v.quote}\"")
                print(f"Fix: {v.recommendation}")

    # Files that pass
    files_with_violations = set(violations_by_file.keys())
    clean_files = [f for f in files_checked if str(f) not in files_with_violations]

    print("\n" + "=" * 80)
    print(f"CLEAN FILES ({len(clean_files)} files)")
    print("=" * 80)
    print("\nThe following files pass all tenet checks:")
    for file_path in sorted(clean_files):
        print(f"  ✓ {file_path.name}")

    print("\n" + "=" * 80)
    print("END REPORT")
    print("=" * 80)


if __name__ == "__main__":
    main()
