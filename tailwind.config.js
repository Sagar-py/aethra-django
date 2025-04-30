/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './aethra_project/templates/**/*.html',
    './reviews/templates/**/*.html',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Helvetica', 'sans-serif'],
      },
      colors: {
        saffron: '#D9A441',
        charcoal: '#2C2C2C',
        teal: '#86A8A5',
        nearblack: '#1F1F1F',
        olivegray: '#99988F',
        bgsoft: '#FAFAFA',
        bordergray: '#E6E4DE',
        linkblue: '#4C6A92',
        quote: '#F5F3EF',
        embed: '#F8F8F6',
        tableheader: '#ECE9E4',
      },
    },
  },
  plugins: [],
}
