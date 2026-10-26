import { Download, GitBranch, Package } from "lucide-react";
import { SITE } from "@/lib/metadata";

export default function DownloadPage() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-16">
      <h1 className="text-4xl font-bold mb-4">Download {SITE.name}</h1>
      <p className="text-xl text-gray-600 dark:text-gray-400 mb-12">
        Choose the package that fits your needs
      </p>

      <div className="grid gap-6 md:grid-cols-2">
        {/* Complete Family */}
        <div className="border border-gray-200 dark:border-gray-800 rounded-lg p-6 hover:border-gray-300 dark:hover:border-gray-700 transition-colors">
          <div className="flex items-center gap-3 mb-4">
            <Package className="h-8 w-8 text-gray-900 dark:text-white" />
            <h2 className="text-xl font-semibold">Complete Family</h2>
          </div>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            All font families, weights, and formats in one package
          </p>
          <ul className="text-sm text-gray-500 dark:text-gray-500 mb-6 space-y-1">
            <li>• Khulna Sans (all weights)</li>
            <li>• Khulna Mono</li>
            <li>• Khulna Pixel</li>
            <li>• Variable fonts</li>
            <li>• All formats (TTF, WOFF2, OTF)</li>
          </ul>
          <a
            href={`${SITE.repo}/releases`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-4 py-2 bg-gray-900 dark:bg-white text-white dark:text-black rounded-lg hover:bg-gray-800 dark:hover:bg-gray-200 transition-colors"
          >
            <Download className="h-4 w-4" />
            Download
          </a>
        </div>

        {/* Web Fonts */}
        <div className="border border-gray-200 dark:border-gray-800 rounded-lg p-6 hover:border-gray-300 dark:hover:border-gray-700 transition-colors">
          <div className="flex items-center gap-3 mb-4">
            <Package className="h-8 w-8 text-gray-900 dark:text-white" />
            <h2 className="text-xl font-semibold">Web Fonts</h2>
          </div>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Optimized WOFF2 formats for web use
          </p>
          <ul className="text-sm text-gray-500 dark:text-gray-500 mb-6 space-y-1">
            <li>• Khulna Sans WOFF2</li>
            <li>• Khulna Mono WOFF2</li>
            <li>• Subset for smaller file size</li>
            <li>• CSS @font-face rules included</li>
          </ul>
          <a
            href={`${SITE.repo}/releases`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-4 py-2 bg-gray-900 dark:bg-white text-white dark:text-black rounded-lg hover:bg-gray-800 dark:hover:bg-gray-200 transition-colors"
          >
            <Download className="h-4 w-4" />
            Download
          </a>
        </div>

        {/* Variable Fonts */}
        <div className="border border-gray-200 dark:border-gray-800 rounded-lg p-6 hover:border-gray-300 dark:hover:border-gray-700 transition-colors">
          <div className="flex items-center gap-3 mb-4">
            <Package className="h-8 w-8 text-gray-900 dark:text-white" />
            <h2 className="text-xl font-semibold">Variable Fonts</h2>
          </div>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            Variable font files with adjustable axes
          </p>
          <ul className="text-sm text-gray-500 dark:text-gray-500 mb-6 space-y-1">
            <li>• Khulna Sans Variable</li>
            <li>• Weight axis (100-900)</li>
            <li>• Single file, multiple weights</li>
            <li>• Modern browser support</li>
          </ul>
          <a
            href={`${SITE.repo}/releases`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-4 py-2 bg-gray-900 dark:bg-white text-white dark:text-black rounded-lg hover:bg-gray-800 dark:hover:bg-gray-200 transition-colors"
          >
            <Download className="h-4 w-4" />
            Download
          </a>
        </div>

        {/* Source Files */}
        <div className="border border-gray-200 dark:border-gray-800 rounded-lg p-6 hover:border-gray-300 dark:hover:border-gray-700 transition-colors">
          <div className="flex items-center gap-3 mb-4">
            <GitBranch className="h-8 w-8 text-gray-900 dark:text-white" />
            <h2 className="text-xl font-semibold">Source Files</h2>
          </div>
          <p className="text-gray-600 dark:text-gray-400 mb-4">
            UFO source files for font designers
          </p>
          <ul className="text-sm text-gray-500 dark:text-gray-500 mb-6 space-y-1">
            <li>• UFO source files</li>
            <li>• Design space files</li>
            <li>• Build scripts</li>
            <li>• Complete development setup</li>
          </ul>
          <a
            href={SITE.repo}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 px-4 py-2 border border-gray-300 dark:border-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
          >
            <GitBranch className="h-4 w-4" />
            View on GitHub
          </a>
        </div>
      </div>

      <div className="mt-12 p-6 bg-gray-50 dark:bg-gray-900 rounded-lg">
        <h3 className="text-lg font-semibold mb-4">Installation</h3>
        <div className="space-y-4 text-sm text-gray-600 dark:text-gray-400">
          <div>
            <h4 className="font-medium text-gray-900 dark:text-white mb-1">
              macOS
            </h4>
            <p>Double-click the font file and click "Install Font"</p>
          </div>
          <div>
            <h4 className="font-medium text-gray-900 dark:text-white mb-1">
              Windows
            </h4>
            <p>Right-click the font file and select "Install"</p>
          </div>
          <div>
            <h4 className="font-medium text-gray-900 dark:text-white mb-1">
              Linux
            </h4>
            <p>Copy font files to ~/.local/share/fonts or /usr/share/fonts</p>
          </div>
        </div>
      </div>
    </div>
  );
}
