"use client";

import { useState } from "react";
import { FontSelector } from "./FontSelector";
import { WeightSlider } from "./WeightSlider";
import { SizeSlider } from "./SizeSlider";
import { GlyphGrid } from "./GlyphGrid";
import { cn } from "@/lib/utils";

const sampleTexts = [
  { label: "Default", text: "Khulna — Typeface by KhulnaSoft" },
  { label: "Alphabet", text: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" },
  { label: "Numbers", text: "0123456789" },
  { label: "Pangram", text: "The quick brown fox jumps over the lazy dog" },
  { label: "Code", text: "function hello() { return 'Hello, World!'; }" },
  { label: "UI Text", text: "Button • Link • Input • Checkbox • Radio" },
];

export function FontTester() {
  const [font, setFont] = useState("Khulna Sans");
  const [weight, setWeight] = useState(400);
  const [size, setSize] = useState(64);
  const [tracking, setTracking] = useState(0);
  const [lineHeight, setLineHeight] = useState(1.5);
  const [text, setText] = useState(sampleTexts[0].text);
  const [dark, setDark] = useState(false);

  const fontFamily = font === "Khulna Mono" ? "monospace" : "sans-serif";

  return (
    <div className="space-y-6">
      {/* Controls */}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4 p-6 bg-gray-50 dark:bg-gray-900 rounded-lg">
        <div>
          <label className="block text-sm font-medium mb-2">Font Family</label>
          <FontSelector value={font} onChange={setFont} />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">Sample Text</label>
          <select
            value={text}
            onChange={(e) => setText(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md bg-white dark:bg-gray-950"
          >
            {sampleTexts.map((sample) => (
              <option key={sample.label} value={sample.text}>
                {sample.label}
              </option>
            ))}
          </select>
        </div>

        <div className="flex items-end">
          <button
            onClick={() => setDark(!dark)}
            className={cn(
              "w-full px-4 py-2 rounded-md transition-colors",
              dark
                ? "bg-gray-800 text-white"
                : "bg-white text-gray-900 border border-gray-300"
            )}
          >
            {dark ? "Light Mode" : "Dark Mode"}
          </button>
        </div>
      </div>

      {/* Sliders */}
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4 p-6 bg-gray-50 dark:bg-gray-900 rounded-lg">
        <WeightSlider value={weight} onChange={setWeight} />
        <SizeSlider value={size} onChange={setSize} />
        <div>
          <label className="block text-sm font-medium mb-2">
            Tracking {tracking}px
          </label>
          <input
            type="range"
            min="-2"
            max="10"
            step="0.5"
            value={tracking}
            onChange={(e) => setTracking(Number(e.target.value))}
            className="w-full"
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-2">
            Line Height {lineHeight}
          </label>
          <input
            type="range"
            min="1"
            max="2.5"
            step="0.1"
            value={lineHeight}
            onChange={(e) => setLineHeight(Number(e.target.value))}
            className="w-full"
          />
        </div>
      </div>

      {/* Preview */}
      <div
        className={cn(
          "p-8 rounded-lg border-2 border-dashed border-gray-300 dark:border-gray-700 transition-colors",
          dark ? "bg-gray-900 text-white" : "bg-white text-black"
        )}
      >
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          style={{
            fontFamily: `"${font}", ${fontFamily}`,
            fontSize: `${size}px`,
            fontWeight: weight,
            letterSpacing: `${tracking}px`,
            lineHeight,
            width: "100%",
            minHeight: 200,
            resize: "vertical",
          }}
          className="w-full bg-transparent border-none outline-none resize-y"
        />
      </div>

      {/* Info */}
      <div className="text-sm text-gray-500 dark:text-gray-500">
        <p>Font: {font} | Weight: {weight} | Size: {size}px | Tracking: {tracking}px | Line Height: {lineHeight}</p>
      </div>

      <GlyphGrid fontFamily={`"${font}", ${fontFamily}`} />
    </div>
  );
}
