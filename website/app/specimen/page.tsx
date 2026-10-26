import { FontTester } from "@/components/FontTester";

export default function SpecimenPage() {
  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-2">Font Specimen</h1>
      <p className="text-gray-600 dark:text-gray-400 mb-8">
        Test and explore Khulna fonts with interactive controls
      </p>
      <FontTester />
    </div>
  );
}
