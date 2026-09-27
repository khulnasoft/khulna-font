export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-8">
      <h1 className="text-6xl font-bold tracking-tight">KHULNA</h1>
      <p className="mt-4 text-xl text-gray-600 dark:text-gray-400">
        Typeface by KhulnaSoft
      </p>
      <p className="mt-2 text-lg text-gray-500 dark:text-gray-500">
        A typeface built for interfaces, code, and the web.
      </p>
      <div className="mt-8 flex gap-4">
        <a
          href="/download"
          className="px-6 py-3 bg-black text-white rounded-lg hover:bg-gray-800 dark:bg-white dark:text-black"
        >
          Download
        </a>
        <a
          href="https://github.com/khulnasoft/khulna"
          className="px-6 py-3 border border-gray-300 rounded-lg hover:bg-gray-100 dark:border-gray-700"
        >
          GitHub
        </a>
      </div>
    </main>
  );
}