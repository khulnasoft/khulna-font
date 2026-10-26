import Link from "next/link";
import { ArrowRight, Download, GitBranch, Code, Globe, Layers } from "lucide-react";
import { SITE } from "@/lib/metadata";

const features = [
  {
    icon: Code,
    title: "Code-Optimized",
    description: "Monospace variant designed for developer tools and code editors",
  },
  {
    icon: Globe,
    title: "Screen-Ready",
    description: "Optimized for digital displays and modern interfaces",
  },
  {
    icon: Layers,
    title: "Variable Fonts",
    description: "Flexible weights and styles in compact variable font format",
  },
];

export default function Home() {
  return (
    <main className="flex-1">
      {/* Hero Section */}
      <section className="py-20 px-4 text-center">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-7xl md:text-8xl font-bold tracking-tight mb-6 font-sans">
            KHULNA
          </h1>
          <p className="text-2xl md:text-3xl text-gray-600 dark:text-gray-400 mb-4">
            {SITE.tagline}
          </p>
          <p className="text-lg text-gray-500 dark:text-gray-500 mb-12 max-w-2xl mx-auto">
            {SITE.description}
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/download"
              className="inline-flex items-center justify-center gap-2 px-8 py-4 bg-gray-900 dark:bg-white text-white dark:text-black rounded-lg hover:bg-gray-800 dark:hover:bg-gray-200 transition-colors text-lg font-medium"
            >
              <Download className="h-5 w-5" />
              Download
            </Link>
            <Link
              href="/specimen"
              className="inline-flex items-center justify-center gap-2 px-8 py-4 border border-gray-300 dark:border-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors text-lg font-medium"
            >
              Try Specimen
              <ArrowRight className="h-5 w-5" />
            </Link>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 px-4 bg-gray-50 dark:bg-gray-900">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Built for Modern Interfaces
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            {features.map((feature) => (
              <div
                key={feature.title}
                className="p-6 bg-white dark:bg-gray-950 rounded-lg border border-gray-200 dark:border-gray-800"
              >
                <feature.icon className="h-8 w-8 text-gray-900 dark:text-white mb-4" />
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-gray-600 dark:text-gray-400">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Font Families Section */}
      <section className="py-16 px-4">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">Font Families</h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="p-6 border border-gray-200 dark:border-gray-800 rounded-lg">
              <h3 className="text-2xl font-bold mb-2 font-sans">Khulna Sans</h3>
              <p className="text-gray-600 dark:text-gray-400 mb-4">
                Versatile sans-serif for interfaces and general use
              </p>
              <Link
                href="/specimen"
                className="text-sm text-gray-900 dark:text-white hover:underline inline-flex items-center gap-1"
              >
                Try it <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
            <div className="p-6 border border-gray-200 dark:border-gray-800 rounded-lg">
              <h3 className="text-2xl font-bold mb-2 font-mono">Khulna Mono</h3>
              <p className="text-gray-600 dark:text-gray-400 mb-4">
                Monospace variant optimized for code
              </p>
              <Link
                href="/specimen"
                className="text-sm text-gray-900 dark:text-white hover:underline inline-flex items-center gap-1"
              >
                Try it <ArrowRight className="h-4 w-4" />
              </Link>
            </div>
            <div className="p-6 border border-gray-200 dark:border-gray-800 rounded-lg opacity-60">
              <h3 className="text-2xl font-bold mb-2">Khulna Pixel</h3>
              <p className="text-gray-600 dark:text-gray-400 mb-4">
                Pixel variant for retro designs (Coming Soon)
              </p>
              <span className="text-sm text-gray-500">Coming Soon</span>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 px-4 bg-gray-50 dark:bg-gray-900">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Use Khulna?</h2>
          <p className="text-gray-600 dark:text-gray-400 mb-8">
            Download the fonts and start using them in your projects today.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/download"
              className="inline-flex items-center justify-center gap-2 px-8 py-4 bg-gray-900 dark:bg-white text-white dark:text-black rounded-lg hover:bg-gray-800 dark:hover:bg-gray-200 transition-colors text-lg font-medium"
            >
              <Download className="h-5 w-5" />
              Download Fonts
            </Link>
            <a
              href={SITE.repo}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center gap-2 px-8 py-4 border border-gray-300 dark:border-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors text-lg font-medium"
            >
              <GitBranch className="h-5 w-5" />
              View on GitHub
            </a>
          </div>
        </div>
      </section>
    </main>
  );
}
