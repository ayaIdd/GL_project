/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      height:{
       header:'560px',
       rate:'400px'
      },
      fontSize:{
        h1:'2.6rem',
      },
      screens:{
        xs:'475px',
      },
      colors:{
        maincolor:'#E743E0',
      },
    },
  },
  plugins: [
   require( '@tailwindcss/line-clamp'),
  ],
}