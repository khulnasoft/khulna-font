import Link from "next/link";
import { ArrowRight } from "lucide-react";

export default function DocumentationIndex() {
  const sections = [
    {
      title: "Getting Started",
      description: "Learn how to install and use Khulna fonts",
      links: [
        { href: "/documentation/installation", label: "Installation" },
        { href: "/documentation/usage", label: "Usage" },
        { href: "/documentation/web-fonts", label: "Web Fonts" },
      ],
    },
    {
      title: "Reference",
      description: "Detailed technical information about the fonts",
      links: [
        { href: "/documentation/glyphs", label: "Glyph Coverage" },
        { href: "/documentation/unicode", label: "Unicode Support" },
        { href: "/documentation/variable-fonts", label: "Variable Fonts" },
        { href: "/documentation/opentype", label: "OpenType Features" },
      ],
    },
    {
      title: "About",
      description: "Learn about licensing and contributing",
      links: [
        { href: "/documentation/licensing", label: "Licensing" },
        { href: "/documentation/contributing", label: "Contributing" },
      ],
    },
  ];

  return (
    <div>
      <h1 className="text-4xl font-bold mb-4">Documentation</h1>
      <p className="text-xl text-gray-600 dark:text-gray-400 mb-12">
        Everything you need to know about Khulna fonts
      </p>

      <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
        {sections.map((section) => (
          <div
            key={section.title}
            className="border border-gray-200 dark:border-gray-800 rounded-lg p-6"
          >
            <h2 className="text-xl font-semibold mb-2">{section.title}</h2>
            <p className="text-gray-600 dark:text-gray-400 mb-4">
              {section.description}
            </p>
            <ul className="space-y-2">
              {section.links.map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
                  >
                    {link.label}
                    <ArrowRight className="h-4 w-4" />
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
