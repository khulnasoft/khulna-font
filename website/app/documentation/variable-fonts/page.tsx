export default function VariableFontsPage() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Variable Fonts</h1>

      <div className="prose dark:prose-invert max-w-none">
        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Supported Axes</h2>
          <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
            <li>
              <strong>wght</strong> - Weight (100–900)
            </li>
            <li>
              <strong>wdth</strong> - Width
            </li>
            <li>
              <strong>slnt</strong> - Slant
            </li>
            <li>
              <strong>opsz</strong> - Optical Size
            </li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Variable Font Files</h2>
          <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
            <li>KhulnaSans[wght].woff2</li>
            <li>KhulnaMono[wght].woff2</li>
          </ul>
        </section>
      </div>
    </div>
  );
}