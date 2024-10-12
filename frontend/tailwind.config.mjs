// tailwind.config.mjs
export default {
  theme: {
    extend: {
      colors: {
        primary: '#1e3a8a',
        secondary: '#0a0e14',
        accent: '#4b5563',
        background: '#0f172a',
        surface: '#1f2937',
        highlight: '#334155', /* Slightly lighter for hover states */
      },
      borderRadius: {
        'lg': '12px',
        'xl': '16px',
      },
      boxShadow: {
        'glow': '0 0 15px rgba(255, 255, 255, 0.1)',
        'deep': '0 4px 15px rgba(0, 0, 0, 0.8)',
      },
      fontFamily: {
        'body': ['Roboto', 'sans-serif'],
        'title': ['Montserrat', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
