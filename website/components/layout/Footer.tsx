import Link from "next/link";
import { GitBranch, Download } from "lucide-react";
import { SITE } from "@/lib/metadata";

export function Footer() {
  return (
    <footer className="border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Brand */}
          <div>
            <h3 className="text-lg font-bold font-sans mb-2">{SITE.name}</h3>
            <p className="text-sm text-gray-600 dark:text-gray-400">
              {SITE.tagline}
            </p>
            <p className="text-sm text-gray-500 dark:text-gray-500 mt-1">
              {SITE.description}
            </p>
          </div>

          {/* Links */}
          <div>
            <h4 className="text-sm font-semibold mb-3">Links</h4>
            <ul className="space-y-2 text-sm">
              <li>
                <Link
                  href="/specimen"
                  className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
                >
                  Specimen
                </Link>
              </li>
              <li>
                <Link
                  href="/documentation"
                  className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
                >
                  Documentation
                </Link>
              </li>
              <li>
                <Link
                  href="/download"
                  className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
                >
                  Download
                </Link>
              </li>
              <li>
                <Link
                  href="/about"
                  className="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
                >
                  About
                </Link>
              </li>
            </ul>
          </div>

          {/* Resources */}
          <div>
            <h4 className="text-sm font-semibold mb-3">Resources</h4>
            <ul className="space-y-2 text-sm">
              <li>
                <a
                  href={SITE.repo}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
                >
                  <GitBranch className="h-4 w-4" />
                  GitHub Repository
                </a>
              </li>
              <li>
                <Link
                  href="/download"
                  className="flex items-center gap-2 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
                >
                  <Download className="h-4 w-4" />
                  Download Fonts
                </Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-gray-200 dark:border-gray-800 text-center text-sm text-gray-500 dark:text-gray-500">
          <p>
            &copy; {new Date().getFullYear()} KhulnaSoft. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
