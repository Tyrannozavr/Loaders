// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    ssr: true,
    compatibilityDate: '2024-04-03',
    devtools: {enabled: true},
    modules: ['@nuxt/ui', '@samk-dev/nuxt-vcalendar'],
    colorMode: {
        preference: 'light'
    },
    runtimeConfig: {
        public: {
            baseURL: process.env.NUXT_API_URL,
        }
    },
})