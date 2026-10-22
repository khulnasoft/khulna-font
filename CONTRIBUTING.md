# Contributing to Khulna

Thank you for your interest in contributing to Khulna — Typeface by KhulnaSoft.

## Setup

```bash
pnpm install
pnpm build
pnpm validate
```

## Development

- Font sources live in `fonts/KhulnaSans/sources/`, `fonts/KhulnaMono/sources/`
- Build scripts are in `scripts/`
- Tests are in `tests/`
- Website runs with `pnpm dev`

## Pull Requests

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `pnpm check` (lint + test + validate)
5. Submit a PR with a clear description

## Font Changes

- Update source files in the appropriate `sources/` directory
- Rebuild with `pnpm build:fonts`
- Run validation with `pnpm validate`
- Ensure FontBakery checks pass

## Code Style

- TypeScript for all scripts
- Prettier for formatting
- ESLint for linting

## Questions

Open an issue before starting significant work to discuss approach.
