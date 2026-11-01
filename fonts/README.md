# Portfolio typography

- **Headings and metrics:** installed NDot, then bundled **Portfolio Dot**, an original five-by-seven round-dot display font. Portfolio Dot is not NDot, a Nothing font, or the linked FontStruct font. Lowercase characters intentionally use capital display glyphs. Other scripts and unsupported symbols fall back to the next font.
- **Body:** installed NType 82, then the existing system sans-serif stack.
- **Labels and navigation:** installed NType 82 Mono, then system monospace.

Portfolio Dot is self-hosted as `PortfolioDot.woff`; it requires no third-party font requests. Its source is `../tools/build_dot_font.py` and its license is `LICENSE-PortfolioDot.txt`. Rebuild from the repository root with `python3 tools/build_dot_font.py` (requires Python fontTools). No build is needed to serve the checked-in WOFF.

Exact NDot, NType 82 and NType 82 Mono webfonts are not included. Public download availability does not establish redistribution rights. If authorized files become available, add their real URLs and correct static weights or variable ranges to the matching `@font-face` declarations in `styles.css`. The current local-only declarations avoid requests for nonexistent files.

## FontStruct review status — 1 November 2026

Requested URL: https://fontstruct.com/fontstructions/download/2047444

The environment proxy returned HTTP 403 during CONNECT. No website content, redirects, certificate chain, license, archive or font binary was received. That response is a network restriction, not evidence that FontStruct is malicious or safe. No malware verdict is possible from this check. Antivirus and OpenType Sanitizer tools were not installed.

Before incorporating that download: obtain access via environment settings, fetch over verified HTTPS, inspect redirects and file signatures, list archive entries without running anything, verify the author/license permits web embedding and distribution, validate the font structure, and scan the actual file with up-to-date security tooling. Record its SHA-256. A clean scan is limited evidence, not a guarantee of safety.

The bundled Portfolio Dot is generated locally from the readable source, independently of the inaccessible download. It contains standard outline, metrics and naming tables only; it has no TrueType instruction bytecode, embedded SVG, bitmap assets or external resource references. Structural validation is not an antivirus scan.
