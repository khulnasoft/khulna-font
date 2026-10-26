# Khulna Font Website - Implementation Plan

## Overview
A comprehensive plan to build the specimen website for the Khulna typeface family, showcasing Khulna Sans, Khulna Mono, and Khulna Pixel with interactive testing, documentation, and download capabilities.

---

## Phase 1: Core Structure & Navigation

### 1.1 Navigation System
- [ ] Implement responsive navigation bar
  - Logo/brand name
  - Links: Home, Specimen, Documentation, About
  - Dark mode toggle
  - Mobile hamburger menu

### 1.2 Route Structure
```
/                    - Landing page
/specimen            - Interactive font tester
/documentation       - Documentation pages
/about               - About page
/download            - Download page with file options
```

### 1.3 Layout Components
- [ ] Create shared `<Navbar />` component
- [ ] Create shared `<Footer />` component
- [ ] Update `layout.tsx` to include navigation
- [ ] Add dark mode context/provider

---

## Phase 2: Landing Page Enhancement

### 2.1 Hero Section
- [ ] Large typography showcase using Khulna fonts
- [ ] Animated gradient or subtle motion effects
- [ ] Clear CTA buttons (Download, Try Specimen)
- [ ] Font family preview cards

### 2.2 Feature Highlights
- [ ] Grid showcasing font features:
  - Screen-optimized for interfaces
  - Code-friendly monospace
  - Variable font support
  - Multi-language support
  - Pixel variant for retro designs

### 2.3 Quick Preview
- [ ] Mini interactive preview component
- [ ] Sample text with different font families
- [ ] Size/weight quick toggle

---

## Phase 3: Specimen Page (Interactive Font Tester)

### 3.1 Enhanced FontTester Component
- [ ] Integrate existing sliders (SizeSlider, WeightSlider)
- [ ] Add tracking/letter-spacing control
- [ ] Add line-height control
- [ ] Add real-time preview updates
- [ ] Dark/light mode toggle for preview area

### 3.2 Font Family Integration
- [ ] Load actual font files from `dist/` directory
- [ ] Configure CSS font-face rules for:
  - Khulna Sans (static + variable)
  - Khulna Mono
  - Khulna Pixel (when available)
- [ ] Fallback chain for graceful degradation

### 3.3 Sample Text Presets
- [ ] Dropdown with sample texts:
  - Alphabet (A-Z, a-z)
  - Numbers & symbols
  - Pangrams
  - Code snippets
  - UI text samples
  - Multi-language samples

### 3.4 Glyph Grid Implementation
- [ ] Complete `GlyphGrid.tsx` component
- [ ] Display all available glyphs
- [ ] Filterable by character set (Latin, Greek, symbols)
- [ ] Click-to-copy functionality
- [ ] Grid responsive layout

### 3.5 Comparison View
- [ ] Side-by-side font comparison
- [ ] Sync controls across panels
- [ ] Split slider for visual comparison

---

## Phase 4: Documentation Pages

### 4.1 Documentation Structure
- [ ] Create `/documentation` layout
- [ ] Sidebar navigation for docs sections
- [ ] Markdown content rendering (use next/mdx or similar)

### 4.2 Documentation Content
Convert existing docs to web pages:
- [ ] Installation guide (from `docs/installation.md`)
- [ ] Usage examples (CSS, @font-face, variable fonts)
- [ ] Glyph coverage (from `docs/glyphs.md`)
- [ ] Unicode support (from `docs/unicode.md`)
- [ ] Variable font axes (from `docs/variable-fonts.md`)
- [ ] Web fonts integration (from `docs/web-fonts.md`)
- [ ] Licensing info (from `docs/licensing.md`)

### 4.3 Code Examples
- [ ] Syntax-highlighted code blocks
- [ ] Copy-to-clipboard functionality
- [ ] Live preview where applicable

---

## Phase 5: Download Page

### 5.1 Download Options
- [ ] Package selection:
  - Complete family (all weights, formats)
  - Individual families (Sans, Mono, Pixel)
  - Web font package (WOFF2 only)
  - Variable fonts only
- [ ] File format options: TTF, WOFF2, OTF

### 5.2 Download Component
- [ ] Enhance `DownloadButton.tsx` with:
  - File size display
  - Format badges
  - Version info
- [ ] Add download analytics (optional)

### 5.3 Installation Instructions
- [ ] Quick start guide
- [ ] Platform-specific instructions (macOS, Windows, Linux)
- [ ] Integration with popular tools (Figma, Sketch, VS Code)

---

## Phase 6: About Page

### 6.1 Project Information
- [ ] Project history and goals
- [ ] Team/contributors section
- [ ] Design philosophy
- [ ] Roadmap

### 6.2 Links & Resources
- [ ] GitHub repository
- [ ] Issue tracker
- [ ] Contributing guidelines
- [ ] Changelog

---

## Phase 7: Technical Enhancements

### 7.1 Font Loading Optimization
- [ ] Implement font subsetting
- [ ] Use `font-display: swap` strategy
- [ ] Critical font inlining for LCP
- [ ] Preload key font files

### 7.2 Performance
- [ ] Image optimization (Next.js Image component)
- [ ] Code splitting for routes
- [ ] Lazy load heavy components
- [ ] Bundle size optimization

### 7.3 SEO & Metadata
- [ ] Dynamic metadata per page
- [ ] Open Graph tags
- [ ] Twitter Card tags
- [ ] Structured data (JSON-LD)
- [ ] Sitemap generation

### 7.4 Accessibility
- [ ] ARIA labels for interactive components
- [ ] Keyboard navigation support
- [ ] Focus management
- [ ] Color contrast compliance
- [ ] Screen reader announcements

---

## Phase 8: Polish & Testing

### 8.1 Responsive Design
- [ ] Mobile-first approach
- [ ] Tablet breakpoints
- [ ] Desktop enhancements
- [ ] Touch-friendly controls

### 8.2 Dark Mode
- [ ] System preference detection
- [ ] Manual toggle with persistence
- [ ] Smooth transitions
- [ ] Custom scrollbar styling

### 8.3 Testing
- [ ] Component unit tests (Vitest)
- [ ] E2E tests for critical flows (Playwright)
- [ ] Cross-browser testing
- [ ] Performance audits (Lighthouse)

### 8.4 Deployment
- [ ] Verify Vercel configuration
- [ ] Set up environment variables
- [ ] Configure custom domain (if applicable)
- [ ] Set up build caching strategy

---

## Priority Order

### High Priority (MVP)
1. Navigation & routing
2. Landing page enhancement
3. Functional specimen page with font loading
4. Download page
5. Basic documentation pages

### Medium Priority
6. Dark mode implementation
7. Glyph grid completion
8. Comparison view
9. About page

### Low Priority (Polish)
10. Advanced documentation features
11. Performance optimization
12. Accessibility enhancements
13. Analytics

---

## Dependencies to Add

### Likely Needed
- `next-themes` - Dark mode management
- `clsx` / `tailwind-merge` - Class name utilities
- `lucide-react` - Icon set
- `@mdx-js/loader` / `next-mdx-remote` - Markdown rendering
- `prism-react-renderer` or `shiki` - Code syntax highlighting
- `framer-motion` - Animations (optional)

### Verification Needed
- Check if Tailwind is properly configured
- Verify font file paths in build output
- Confirm Vercel deployment settings

---

## File Structure After Implementation

```
website/
├── app/
│   ├── layout.tsx          # Root layout with nav/footer
│   ├── page.tsx            # Landing page
│   ├── specimen/
│   │   └── page.tsx        # Font tester
│   ├── documentation/
│   │   ├── layout.tsx      # Docs layout with sidebar
│   │   ├── installation/
│   │   │   └── page.tsx
│   │   ├── usage/
│   │   │   └── page.tsx
│   │   └── ...
│   ├── download/
│   │   └── page.tsx
│   └── about/
│       └── page.tsx
├── components/
│   ├── ui/                 # Reusable UI components
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   ├── Slider.tsx
│   │   └── ...
│   ├── layout/
│   │   ├── Navbar.tsx
│   │   ├── Footer.tsx
│   │   └── Sidebar.tsx
│   ├── specimen/
│   │   ├── FontTester.tsx  # Enhanced
│   │   ├── GlyphGrid.tsx   # Completed
│   │   ├── ComparisonView.tsx
│   │   └── SampleTexts.tsx
│   └── DownloadButton.tsx  # Enhanced
├── lib/
│   ├── fonts.ts            # Font configuration
│   ├── metadata.ts         # Site metadata
│   └── utils.ts            # Utility functions
├── public/
│   └── fonts/              # Font files (or served from dist/)
└── styles/
    └── globals.css         # Global styles with font-face
```

---

## Next Steps

1. **Review this plan** with the team to confirm priorities
2. **Set up Tailwind configuration** if not already done
3. **Create font-face rules** in globals.css for all font variants
4. **Begin Phase 1** - Navigation & routing
5. **Iterate based on feedback** after each phase

---

## Notes

- The website currently has `typescript: { ignoreBuildErrors: true }` in `next.config.ts` - this should be removed and type errors fixed
- Font files need to be accessible to the Next.js app - either copy to `public/fonts/` or configure static file serving from `dist/`
- Consider using the actual font files from the build process rather than stubs
- The build command `pnpm build` builds fonts, packages, and website - ensure this workflow is maintained
