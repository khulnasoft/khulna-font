# Architecture

## Repository Structure

```
khulna/
├── fonts/          Source fonts and build output
├── packages/       npm packages
├── website/        Specimen website
├── scripts/        Build scripts
├── tests/          Test suites
├── tools/          Tooling
└── docs/           Documentation
```

## Build Pipeline

Source Fonts → Font Compilation → OpenType Build → Variable/Static Fonts → WOFF2 → npm/Website/CDN
