export const FONTS = [
  { name: "Khulna Sans", css: '"Khulna Sans", sans-serif' },
  { name: "Khulna Mono", css: '"Khulna Mono", monospace' },
];

export function getFontCss(name: string) {
  return FONTS.find((f) => f.name === name)?.css ?? FONTS[0].css;
}