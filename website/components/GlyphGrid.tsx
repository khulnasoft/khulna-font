"use client";

import { useMemo, useState } from "react";
import { cn } from "@/lib/utils";

const glyphSets = {
  Latin: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
  Greek: "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω",
  Symbols: "!@#$%^&*()[]{}<>+-=*/\\|~`_.,:;?€£¥¢§©®™←↑→↓",
} as const;

type GlyphSet = keyof typeof glyphSets;

interface GlyphGridProps {
  fontFamily: string;
}

export function GlyphGrid({ fontFamily }: GlyphGridProps) {
  const [set, setSet] = useState<GlyphSet>("Latin");
  const [copied, setCopied] = useState<string | null>(null);
  const glyphs = useMemo(() => Array.from(glyphSets[set]), [set]);

  async function copyGlyph(glyph: string) {
    try {
      await navigator.clipboard.writeText(glyph);
      setCopied(glyph);
    } catch {
      setCopied(null);
    }
  }

  return (
    <section aria-labelledby="glyph-grid-heading" className="space-y-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <div>
          <h2 id="glyph-grid-heading" className="text-2xl font-semibold">
            Glyphs
          </h2>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            Select a glyph to copy it to your clipboard.
          </p>
        </div>
        <div className="flex gap-2" aria-label="Glyph category">
          {(Object.keys(glyphSets) as GlyphSet[]).map((name) => (
            <button
              key={name}
              type="button"
              onClick={() => setSet(name)}
              aria-pressed={set === name}
              className={cn(
                "rounded-md px-3 py-2 text-sm font-medium transition-colors",
                set === name
                  ? "bg-gray-900 text-white dark:bg-white dark:text-gray-900"
                  : "border border-gray-300 hover:bg-gray-100 dark:border-gray-700 dark:hover:bg-gray-800"
              )}
            >
              {name}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-6 gap-2 sm:grid-cols-8 md:grid-cols-10 lg:grid-cols-12">
        {glyphs.map((glyph) => (
          <button
            key={glyph}
            type="button"
            onClick={() => void copyGlyph(glyph)}
            title={`Copy ${glyph} (U+${glyph.codePointAt(0)?.toString(16).toUpperCase().padStart(4, "0")})`}
            className="aspect-square rounded-md border border-gray-200 bg-white text-2xl transition-colors hover:border-gray-900 hover:bg-gray-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-gray-900 dark:border-gray-800 dark:bg-gray-950 dark:hover:border-white dark:hover:bg-gray-900 dark:focus-visible:ring-white"
            style={{ fontFamily }}
          >
            {glyph}
          </button>
        ))}
      </div>
      <p className="sr-only" aria-live="polite">
        {copied ? `${copied} copied to clipboard.` : ""}
      </p>
    </section>
  );
}
