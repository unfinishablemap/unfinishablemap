#!/usr/bin/env python3
"""
Manual tenet violation check with context-aware analysis.
Focuses on actual endorsements rather than mere discussion of opposing views.
"""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Issue:
    file_path: str
    severity: str  # ERROR, WARNING, NOTE
    tenet: str
    description: str
    quote: str
    line_range: str
    recommendation: str


def is_critical_context(text_before: str, text_after: str) -> bool:
    """Check if surrounding text indicates critique rather than endorsement."""
    combined = (text_before + " " + text_after).lower()

    critical_markers = [
        r'\breject\b', r'\bdismiss\b', r'\bfails?\b', r'\bwrong\b',
        r'\bobjection\b', r'\bproblem\b', r'\bchallenge\b',
        r'\bdifficult(y|ies)\b', r'\bdefeat\b', r'\bundermin\w+\b',
        r'\bself-stultif\w+\b', r'\bself-defeat\w+\b',
        r'\bincoherent\b', r'\bregress\b', r'\bcritique\b',
        r'\bflawed\b', r'\bmistaken\b', r'\bdoubtful\b',
        r'\bif\b.*\btrue\b', r'\bif\b.*\bcorrect\b',  # hypothetical
        r'\baccording to\b', r'\bproponents\b', r'\b(claim|argue|hold) that\b',
        r'\bthe view that\b', r'\bthe position that\b',
        r'\bwould say\b', r'\bwould hold\b', r'\bwould argue\b',
        r'\b(question|doubt|deny|dispute)\b',
    ]

    for pattern in critical_markers:
        if re.search(pattern, combined):
            return True
    return False


def check_for_mwi_endorsement(content: str, filepath: str) -> List[Issue]:
    """Check for endorsement of many-worlds interpretation."""
    issues = []

    # Skip dedicated MWI article (it's allowed to explain the view)
    if 'many-worlds.md' in filepath:
        return issues

    # Look for endorsement patterns
    endorsement_patterns = [
        (r'many[- ]worlds?\s+(is\s+correct|solves?|explains?|shows?)',
         "Appears to endorse MWI"),
        (r'all\s+branches\s+are\s+(equally\s+)?real',
         "Endorses MWI ontology"),
    ]

    for pattern, desc in endorsement_patterns:
        for match in re.finditer(pattern, content, re.IGNORECASE):
            start = max(0, match.start() - 300)
            end = min(len(content), match.end() + 300)
            context_before = content[start:match.start()]
            context_after = content[match.end():end]

            if not is_critical_context(context_before, context_after):
                quote = content[max(0, match.start()-100):min(len(content), match.end()+100)]
                quote = re.sub(r'\s+', ' ', quote).strip()
                issues.append(Issue(
                    file_path=filepath,
                    severity="ERROR",
                    tenet="No Many Worlds",
                    description=desc,
                    quote=quote[:200] + "..." if len(quote) > 200 else quote,
                    line_range="",
                    recommendation="Add critique or clarify this is rejected per tenets"
                ))

    return issues


def check_for_occam_misuse(content: str, filepath: str) -> List[Issue]:
    """Check for using Occam's Razor decisively against dualism."""
    issues = []

    patterns = [
        (r'dualism\s+(violates|fails)\s+occam',
         "Uses Occam's Razor against dualism"),
        (r'(physicalism|materialism)\s+is\s+simpler,?\s+(therefore|so|thus)',
         "Uses simplicity as decisive argument"),
        (r'we\s+should\s+(prefer|accept|choose)\s+(materialism|physicalism)\s+because\s+it.{1,20}simpler',
         "Uses parsimony decisively"),
    ]

    for pattern, desc in patterns:
        for match in re.finditer(pattern, content, re.IGNORECASE):
            start = max(0, match.start() - 300)
            end = min(len(content), match.end() + 300)
            context_before = content[start:match.start()]
            context_after = content[match.end():end]

            if not is_critical_context(context_before, context_after):
                quote = content[max(0, match.start()-100):min(len(content), match.end()+100)]
                quote = re.sub(r'\s+', ' ', quote).strip()
                issues.append(Issue(
                    file_path=filepath,
                    severity="ERROR",
                    tenet="Occam's Razor Has Limits",
                    description=desc,
                    quote=quote[:200] + "..." if len(quote) > 200 else quote,
                    line_range="",
                    recommendation="Acknowledge Occam's Razor is not decisive"
                ))

    return issues


def check_for_physicalism_assumptions(content: str, filepath: str) -> List[Issue]:
    """Check for assuming physicalism without acknowledgment."""
    issues = []

    # Look for production language without qualification
    patterns = [
        r'the\s+brain\s+(generates|produces|creates)\s+consciousness',
        r'consciousness\s+(emerges|arises)\s+from\s+(complexity|neural)',
        r'consciousness\s+is\s+(generated|produced)\s+by\s+the\s+brain',
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, content, re.IGNORECASE):
            start = max(0, match.start() - 400)
            end = min(len(content), match.end() + 400)
            context = content[start:end]

            # Check for qualifying language nearby
            qualifiers = [
                r'\b(if|assume|hypothetically|suppose)\b',
                r'\bfrom\s+a\s+(physicalist|materialist)\s+perspective\b',
                r'\bon\s+the\s+(physicalist|materialist)\s+view\b',
                r'\bfilter\s+theory\b', r'\binterface\b',
                r'\bor\s+(filter|select|modulate|interface)\b',
            ]

            has_qualifier = any(re.search(q, context, re.IGNORECASE) for q in qualifiers)

            if not has_qualifier and not is_critical_context(
                content[start:match.start()],
                content[match.end():end]
            ):
                quote = content[max(0, match.start()-80):min(len(content), match.end()+80)]
                quote = re.sub(r'\s+', ' ', quote).strip()
                issues.append(Issue(
                    file_path=filepath,
                    severity="WARNING",
                    tenet="Dualism",
                    description="Assumes brain produces consciousness without qualification",
                    quote=quote[:200] + "..." if len(quote) > 200 else quote,
                    line_range="",
                    recommendation="Add qualifier or acknowledge this assumes physicalism"
                ))

    return issues


def check_quantum_mysticism(content: str, filepath: str) -> List[Issue]:
    """Check for quantum mysticism endorsement."""
    issues = []

    # Skip quantum-consciousness.md which discusses mechanisms properly
    if 'quantum-consciousness.md' in filepath:
        return issues

    patterns = [
        (r'quantum\s+(healing|magic)', "Quantum pseudoscience"),
        (r'consciousness\s+creates\s+reality', "Quantum mysticism claim"),
    ]

    for pattern, desc in patterns:
        for match in re.finditer(pattern, content, re.IGNORECASE):
            start = max(0, match.start() - 200)
            end = min(len(content), match.end() + 200)
            context_before = content[start:match.start()]
            context_after = content[match.end():end]

            if not is_critical_context(context_before, context_after):
                quote = content[max(0, match.start()-100):min(len(content), match.end()+100)]
                quote = re.sub(r'\s+', ' ', quote).strip()
                issues.append(Issue(
                    file_path=filepath,
                    severity="ERROR",
                    tenet="Minimal Quantum Interaction",
                    description=desc,
                    quote=quote[:200] + "..." if len(quote) > 200 else quote,
                    line_range="",
                    recommendation="Remove or clearly critique quantum mysticism"
                ))

    return issues


def check_file(file_path: Path) -> List[Issue]:
    """Check a single file for genuine tenet violations."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

    issues = []
    filepath = str(file_path)

    # Skip checking files that are explicitly ABOUT the rejected views
    # (they're allowed to explain them in detail)
    skip_patterns = [
        'illusionism.md',
        'epiphenomenalism.md',
        'materialism.md',
        'many-worlds.md',
        'functionalism.md',
    ]

    filename = file_path.name
    if filename in skip_patterns:
        return issues

    # Run checks
    issues.extend(check_for_mwi_endorsement(content, filepath))
    issues.extend(check_for_occam_misuse(content, filepath))
    issues.extend(check_for_physicalism_assumptions(content, filepath))
    issues.extend(check_quantum_mysticism(content, filepath))

    return issues


def main():
    base_path = Path("/home/andy/unfin/unfinishablemap/obsidian")
    topics_path = base_path / "topics"
    concepts_path = base_path / "concepts"

    all_issues = []
    files_checked = []

    for directory in [topics_path, concepts_path]:
        for file_path in directory.glob("*.md"):
            files_checked.append(file_path)
            issues = check_file(file_path)
            all_issues.extend(issues)

    # Generate report
    print("=" * 80)
    print("TENET VIOLATION ANALYSIS - CONTEXT-AWARE")
    print("=" * 80)
    print()
    print("This analysis distinguishes between:")
    print("- Discussing opposing views (allowed)")
    print("- Endorsing positions that contradict tenets (violations)")
    print()

    errors = [i for i in all_issues if i.severity == "ERROR"]
    warnings = [i for i in all_issues if i.severity == "WARNING"]
    notes = [i for i in all_issues if i.severity == "NOTE"]

    print(f"Files checked: {len(files_checked)}")
    print(f"Issues found: {len(all_issues)}")
    print(f"  - ERRORS (direct contradictions): {len(errors)}")
    print(f"  - WARNINGS (implicit conflicts): {len(warnings)}")
    print(f"  - NOTES (needs clarification): {len(notes)}")
    print()

    if all_issues:
        print("=" * 80)
        print("ISSUES BY FILE")
        print("=" * 80)

        issues_by_file = {}
        for issue in all_issues:
            fname = Path(issue.file_path).name
            if fname not in issues_by_file:
                issues_by_file[fname] = []
            issues_by_file[fname].append(issue)

        for filename in sorted(issues_by_file.keys()):
            file_issues = issues_by_file[filename]
            print(f"\n{filename}")
            print("-" * 80)

            for issue in file_issues:
                print(f"\n[{issue.severity}] {issue.tenet}")
                print(f"Issue: {issue.description}")
                print(f"Quote: \"{issue.quote}\"")
                print(f"Fix: {issue.recommendation}")
    else:
        print("=" * 80)
        print("NO VIOLATIONS FOUND")
        print("=" * 80)
        print()
        print("All files either:")
        print("- Align with the five tenets")
        print("- Discuss opposing views while clearly critiquing them")
        print("- Are dedicated articles explaining rejected positions")

    print("\n" + "=" * 80)
    print("END REPORT")
    print("=" * 80)


if __name__ == "__main__":
    main()
