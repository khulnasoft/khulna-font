"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ChevronRight } from "lucide-react";
import { cn } from "@/lib/utils";

const docsNav = [
  {
    title: "Getting Started",
    items: [
      { href: "/documentation/installation", label: "Installation" },
      { href: "/documentation/usage", label: "Usage" },
      { href: "/documentation/web-fonts", label: "Web Fonts" },
    ],
  },
  {
    title: "Reference",
    items: [
      { href: "/documentation/glyphs", label: "Glyph Coverage" },
      { href: "/documentation/unicode", label: "Unicode Support" },
      { href: "/documentation/variable-fonts", label: "Variable Fonts" },
      { href: "/documentation/opentype", label: "OpenType Features" },
    ],
  },
  {
    title: "About",
    items: [
      { href: "/documentation/licensing", label: "Licensing" },
      { href: "/documentation/contributing", label: "Contributing" },
    ],
  },
];

export default function DocumentationLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="flex gap-8">
        {/* Sidebar */}
        <aside className="w-64 flex-shrink-0 hidden lg:block">
          <nav className="sticky top-8 space-y-8">
            {docsNav.map((section) => (
              <div key={section.title}>
                <h3 className="text-sm font-semibold text-gray-900 dark:text-white mb-3">
                  {section.title}
                </h3>
                <ul className="space-y-1">
                  {section.items.map((item) => {
                    const isActive = pathname === item.href;
                    return (
                      <li key={item.href}>
                        <Link
                          href={item.href}
                          className={cn(
                            "flex items-center gap-2 text-sm transition-colors",
                            isActive
                              ? "text-gray-900 dark:text-white font-medium"
                              : "text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white"
                          )}
                        >
                          <ChevronRight
                            className={cn(
                              "h-4 w-4",
                              isActive ? "opacity-100" : "opacity-0"
                            )}
                          />
                          {item.label}
                        </Link>
                      </li>
                    );
                  })}
                </ul>
              </div>
            ))}
          </nav>
        </aside>

        {/* Main content */}
        <div className="flex-1 min-w-0">{children}</div>
      </div>
    </div>
  );
}
