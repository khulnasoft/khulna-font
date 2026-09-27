export function SizeSlider({ value, onChange }: { value: number; onChange: (v: number) => void }) {
  return (
    <label>
      Size
      <input type="range" min="12" max="160" value={value} onChange={(e) => onChange(Number(e.target.value))} />
    </label>
  );
}