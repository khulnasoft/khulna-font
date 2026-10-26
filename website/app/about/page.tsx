import { SITE } from "@/lib/metadata";

export default function AboutPage() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-16">
      <h1 className="text-4xl font-bold mb-8">About {SITE.name}</h1>

      <div className="prose dark:prose-invert max-w-none">
        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-4">Project</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            {SITE.name} is an open-source typeface family designed for modern
            interfaces, developer tools, code, documentation, and the web.
          </p>
          <p className="text-gray-600 dark:text-gray-400">
            Developed by KhulnaSoft, this typeface aims to provide excellent
            readability across various contexts while maintaining a clean,
            modern aesthetic.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-4">Font Families</h2>
          <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
            <li>
              <strong>Khulna Sans</strong> - A versatile sans-serif typeface for
              interfaces and general use
            </li>
            <li>
              <strong>Khulna Mono</strong> - A monospace variant optimized for
              code and technical documentation
            </li>
            <li>
              <strong>Khulna Pixel</strong> - A pixel-based variant for retro
              designs and low-resolution displays
            </li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-4">Design Philosophy</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            {SITE.name} is designed with the following principles in mind:
          </p>
          <ul className="list-disc list-inside space-y-2 text-gray-600 dark:text-gray-400">
            <li>Excellent legibility at small sizes</li>
            <li>Clear distinction between similar characters</li>
            <li>Optimized for screen rendering</li>
            <li>Support for multiple languages and scripts</li>
            <li>Variable font support for flexible typography</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-4">Status</h2>
          <p className="text-gray-600 dark:text-gray-400">
            {SITE.name} is currently under active development. Version{" "}
            {SITE.version} represents the initial release.
          </p>
        </section>

        <section>
          <h2 className="text-2xl font-semibold mb-4">Contributing</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            We welcome contributions! Please see our{" "}
            <a
              href={SITE.repo}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 dark:text-blue-400 hover:underline"
            >
              GitHub repository
            </a>{" "}
            for guidelines on how to contribute.
          </p>
        </section>
      </div>
    </div>
  );
}
