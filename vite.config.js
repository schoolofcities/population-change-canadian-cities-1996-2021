import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
	base: "/population-change-canadian-cities-1996-2021",
	plugins: [svelte()]
})
