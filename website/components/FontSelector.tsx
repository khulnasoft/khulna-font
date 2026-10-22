export function FontSelector({
  value,
  onChange,
}: {
  value: string;
  onChange: (v: string) => void;
}) {
  return (
    <select value={value} onChange={(e) => onChange(e.target.value)}>
      <option value="Khulna Sans">Khulna Sans</option>
      <option value="Khulna Mono">Khulna Mono</option>
    </select>
  );
}
