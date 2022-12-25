/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './src/**/*.{html,css,svelte}',
        "./node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}",
    ],
    theme: {
        colors: {
            "dg": "#b9b9b9",
            "gb": "#93a5b3",
            "db": "#a3b8c9",
            "lg": "#dddbde",
            "lb": "#c7d5e0",
        },
        extend: {},
    },
    plugins: [
        require('flowbite/plugin')
    ],
    darkMode: 'class',
}