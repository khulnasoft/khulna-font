export default function WebFontsPage() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Web Fonts</h1>

      <div className="prose dark:prose-invert max-w-none">
        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Supported Formats</h2>
          <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
            <li>
              <strong>WOFF2</strong> - Primary format, best compression and
              browser support
            </li>
            <li>
              <strong>WOFF</strong> - Legacy format for older browsers
            </li>
            <li>
              <strong>TTF</strong> - TrueType format, broad compatibility
            </li>
            <li>
              <strong>OTF</strong> - OpenType format with advanced features
            </li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">CSS @font-face</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Use the following CSS to include Khulna fonts in your web project:
          </p>
          <div className="bg-gray-900 dark:bg-gray-800 rounded-lg p-4 overflow-x-auto mb-4">
            <pre className="text-sm text-gray-100">
              <code>{`@font-face {
  font-family: "Khulna Sans";
  src: url("KhulnaSans-Regular.woff2") format("woff2"),
       url("KhulnaSans-Regular.woff") format("woff");
  font-weight: 400;
  font-display: swap;
}

@font-face {
  font-family: "Khulna Mono";
  src: url("KhulnaMono-Regular.woff2") format("woff2"),
       url("KhulnaMono-Regular.woff") format("woff");
  font-weight: 400;
  font-display: swap;
}`}</code>
            </pre>
          </div>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Variable Fonts</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            For variable fonts, use a single @font-face declaration with a
            weight range:
          </p>
          <div className="bg-gray-900 dark:bg-gray-800 rounded-lg p-4 overflow-x-auto mb-4">
            <pre className="text-sm text-gray-100">
              <code>{`@font-face {
  font-family: "Khulna Sans";
  src: url("KhulnaSans-VF.woff2") format("woff2-variations");
  font-weight: 100 900;
  font-display: swap;
}`}</code>
            </pre>
          </div>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">font-display Strategy</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            We recommend using <code>font-display: swap</code> to ensure text
            remains visible during font loading. Other options:
          </p>
          <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
            <li>
              <code>swap</code> - Shows fallback immediately, swaps when font
              loads (recommended)
            </li>
            <li>
              <code>block</code> - Briefly hides text, swaps when font loads
            </li>
            <li>
              <code>fallback</code> - Very short block period, then fallback
            </li>
            <li>
              <code>optional</code> - Loads font only if it arrives quickly
            </li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Optimization Tips</h2>
          <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
            <li>Use WOFF2 for best compression</li>
            <li>Subset fonts to include only characters you need</li>
            <li>Preload critical font files in your HTML</li>
            <li>Use variable fonts to reduce HTTP requests</li>
            <li>Consider self-hosting for better performance</li>
          </ul>
        </section>
      </div>
    </div>
  );
}
