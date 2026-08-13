import { useState } from "react";

function App() {

  const [query, setQuery] = useState("");

  function handleSearch() {
    console.log("User Query:", query);
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">

      <div className="w-full max-w-2xl px-4">

        <h1 className="text-4xl font-bold text-center mb-3">
          JOBSCOUT
        </h1>

        <p className="text-center text-gray-600 mb-6">
          Find your next job with AI
        </p>

        <div className="flex gap-2">

          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search for jobs, internships, skills, location..."
            className="flex-1 px-4 py-3 rounded-lg border border-gray-300 
                       focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

          <button
            onClick={handleSearch}
            className="px-6 py-3 bg-blue-600 text-white rounded-lg 
                       hover:bg-blue-700"
          >
            Search
          </button>

        </div>

      </div>

    </div>
  );
}

export default App;