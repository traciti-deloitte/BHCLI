import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#1f2a44",
        sand: "#f5f1ea",
        brass: "#c2a776",
        slate: "#5b6b7a",
        fog: "#eef2f6"
      },
      fontFamily: {
        display: ["var(--font-display)", "ui-sans-serif", "system-ui"],
        body: ["var(--font-body)", "ui-sans-serif", "system-ui"]
      },
      boxShadow: {
        card: "0 10px 30px rgba(31, 42, 68, 0.08)"
      }
    }
  },
  plugins: []
};

export default config;
