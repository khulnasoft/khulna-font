"use client";

import { useState } from "react";

export function FontTester() {
  const [font, setFont] = useState("Khulna Sans");
  const [weight, setWeight] = useState(400);
  const [size, setSize] = useState(64);
  const [tracking, setTracking] = useState(0);
  const [lineHeight, setLineHeight] = useState(1.5);
  const [text, setText] = useState("Khulna — Typeface by KhulnaSoft");
  const [dark, setDark] = useState(false);

  return (
    <section
      className={
        dark ? "bg-gray-900 text-white p-8" : "bg-white text-black p-8"
      }
    >
      <div className="mb-4">
        <label>Font</label>
        <select value={font} onChange={(e) => setFont(e.target.value)}>
          <option value="Khulna Sans">Khulna Sans</option>
          <option value="Khulna Mono">Khulna Mono</option>
        </select>
      </div>

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{
          fontFamily: `"${font}"`,
          fontSize: `${size}px`,
          fontWeight: weight,
          letterSpacing: `${tracking}px`,
          lineHeight,
          width: "100%",
          minHeight: 120,
        }}
      />

      <div className="mt-4 grid grid-cols-2 gap-4">
        <label>
          Weight {weight}
          <input
            type="range"
            min="100"
            max="900"
            step="100"
            value={weight}
            onChange={(e) => setWeight(Number(e.target.value))}
          />
        </label>

        <label>
          Size {size}px
          <input
            type="range"
            min="12"
            max="160"
            value={size}
            onChange={(e) => setSize(Number(e.target.value))}
          />
        </label>

        <label>
          Tracking {tracking}px
          <input
            type="range"
            min="-5"
            max="20"
            value={tracking}
            onChange={(e) => setTracking(Number(e.target.value))}
          />
        </label>

        <label>
          Line Height {lineHeight}
          <input
            type="range"
            min="1"
            max="3"
            step="0.1"
            value={lineHeight}
            onChange={(e) => setLineHeight(Number(e.target.value))}
          />
        </label>
      </div>

      <div className="mt-4 flex gap-4">
        <button onClick={() => setDark(!dark)}>
          {dark ? "Light" : "Dark"}
        </button>
        <button
          onClick={() =>
            navigator.clipboard.writeText(`font-family: "${font}";`)
          }
        >
          Copy CSS
        </button>
      </div>
    </section>
  );
}
