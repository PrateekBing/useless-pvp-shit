/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        "ibm-plex-mono": "'IBM Plex Mono'",
        "press-start-2p": "'Press Start 2P'",
        "sf-alien-encounters": "'SF Alien Encounters'",
      },
    },
    colors: {
      white: "#fff",
      black: "#000",
      indigo: "#2d0485",
      gray: "rgba(217, 217, 217, 0.05)",
      orange: "#fe9900",
    },
    fontSize: { base: "160.16px" },
  },
  corePlugins: { preflight: false },
};
