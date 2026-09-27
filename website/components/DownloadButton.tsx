export function DownloadButton({ href }: { href: string }) {
  return <a href={href} download className="px-4 py-2 border rounded">Download</a>;
}