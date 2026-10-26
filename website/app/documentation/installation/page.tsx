export default function InstallationPage() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Installation</h1>

      <div className="prose dark:prose-invert max-w-none">
        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">npm</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Install Khulna fonts via npm:
          </p>
          <div className="bg-gray-900 dark:bg-gray-800 rounded-lg p-4 overflow-x-auto">
            <code className="text-sm text-gray-100">
              npm install @khulnasoft/khulna
            </code>
          </div>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">CSS Import</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Import the CSS in your stylesheet:
          </p>
          <div className="bg-gray-900 dark:bg-gray-800 rounded-lg p-4 overflow-x-auto">
            <code className="text-sm text-gray-100">
              @import "@khulnasoft/khulna/css";
            </code>
          </div>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Manual Installation</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Download the fonts from the{" "}
            <a
              href="/download"
              className="text-blue-600 dark:text-blue-400 hover:underline"
            >
              download page
            </a>{" "}
            and install them on your system:
          </p>
          <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
            <li>
              <strong>macOS:</strong> Double-click the font file and click
              "Install Font"
            </li>
            <li>
              <strong>Windows:</strong> Right-click the font file and select
              "Install"
            </li>
            <li>
              <strong>Linux:</strong> Copy font files to ~/.local/share/fonts
              or /usr/share/fonts
            </li>
          </ul>
        </section>
      </div>
    </div>
  );
}
