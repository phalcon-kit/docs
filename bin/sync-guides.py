#!/usr/bin/env python3
"""Mirror Core's narrative guides and verify that the published copy is current."""
import argparse
from pathlib import Path
import posixpath
import re
import sys

REPO = Path(__file__).resolve().parents[1]
CORE_URL = 'https://github.com/phalcon-kit/core/blob/master/'


def site_links(text, relative_path):
    core_root_pages = {'README.md', 'CONTRIBUTING.md', 'SUPPORT.md',
                       'SECURITY.md', 'ROADMAP.md', 'CHANGELOG.md'}
    source_parent = posixpath.join('guides', posixpath.dirname(relative_path))

    def rewrite(match):
        destination = match[1]
        location, separator, fragment = destination.partition('#')
        if not location or '://' in location:
            return match[0]
        resolved = posixpath.normpath(posixpath.join(source_parent, location))
        if resolved in core_root_pages or resolved == 'guides/to-be-discussed.md':
            return '](' + CORE_URL + resolved + separator + fragment + ')'
        return match[0]

    return re.sub(r'\]\(([^)\s]+)\)', rewrite, text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--core', type=Path, default=REPO.parent / 'core')
    parser.add_argument('--check', action='store_true', help='Report drift without changing files')
    args = parser.parse_args()
    source = args.core.resolve() / 'guides'
    target = REPO / 'docs' / 'guides'
    if not (source / 'README.md').is_file() or source == target.resolve():
        parser.error('--core must identify a separate Core checkout containing guides/README.md')
    expected = {
        path.relative_to(source).as_posix(): site_links(path.read_text(encoding='utf-8'), path.relative_to(source).as_posix())
        for path in source.rglob('*.md')
    }
    changed = []
    for name, text in sorted(expected.items()):
        path = target / name
        if not path.exists() or path.read_text(encoding='utf-8') != text:
            changed.append(name)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding='utf-8')
    for path in sorted(target.rglob('*.md')):
        name = path.relative_to(target).as_posix()
        if name not in expected:
            changed.append('remove ' + name)
            if not args.check:
                path.unlink()
    if args.check and changed:
        print('Guide drift: ' + ', '.join(changed))
        return 1
    print(('Checked' if args.check else 'Synchronized') + f' {len(expected)} guides; {len(changed)} differences.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
