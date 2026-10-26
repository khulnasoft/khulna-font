export default function UsagePage() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Usage</h1>

      <div className="prose dark:prose-invert max-w-none">
        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Basic Usage</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            After installation, you can use Khulna fonts in your CSS:
          </p>
          <div className="bg-gray-900 dark:bg-gray-800 rounded-lg p-4 overflow-x-auto mb-4">
            <pre className="text-sm text-gray-100">
              <code>{`body {
  font-family: "Khulna Sans", sans-serif;
}

code {
  font-family: "Khulna Mono", monospace;
}`}</code>
            </pre>
          </div>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Font Weights</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Khulna Sans supports weights from 100 to 900:
          </p>
          <div className="bg-gray-900 dark:bg-gray-800 rounded-lg p-4 overflow-x-auto mb-4">
            <pre className="text-sm text-gray-100">
              <code>{`.light { font-weight: 300; }
.regular { font-weight: 400; }
.medium { font-weight: 500; }
.bold { font-weight: 700; }
.black { font-weight: 900; }`}</code>
            </pre>
          </div>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">Variable Fonts</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            With variable fonts, you can use any weight value:
          </p>
          <div className="bg-gray-900 dark:bg-gray-800 rounded-lg p-4 overflow-x-auto mb-4">
            <pre className="text-sm text-gray-100">
              <code>{`.custom-weight {
  font-family: "Khulna Sans", sans-serif;
  font-weight: 475; /* Any value between 100-900 */
}`}</code>
            </pre>
          </div>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">React Example</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Using in a React component:
          </p>
          <div className="bg-gray-900 dark:bg-gray-800 rounded-lg p-4 overflow-x-auto mb-4">
            <pre className="text-sm text-gray-100">
              <code>{`import { KhulnaSans } from '@khulnasoft/khulna';

function App() {
  return (
    <div style={{ fontFamily: KhulnaSans.style.fontFamily }}>
      <h1>Hello, Khulna!</h1>
    </div>
  );
}`}</code>
            </pre>
          </div>
        </section>
      </div>
    </div>
  );
}
