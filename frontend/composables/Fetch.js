import {useFetch} from "#app";
import nuxtStorage from 'nuxt-storage';

const settings = {
    SERVER: true
}

export function getUserToken() {
    return nuxtStorage.get('access_token')
}

export default () => {
    const config = useRuntimeConfig()
    return {
        get: (request, opt = {}) => {
            if (!opt.hasOwnProperty('server')) {
                opt.server = true
            }
            return useFetch(request, {baseURL: config.public.baseURL, ...opt})
        },
        $get: (request, opt) => {
            // console.log('token is', getUserToken())
            return useFetch(request, {
                baseURL: config.public.baseURL, ...opt, server: settings.SERVER,
                onRequest({request, options}) {
                    // Set the request headers
                    options.headers = options.headers || {}
                    options.headers.Authorization = `Token ${getUserToken()}`
                }
            })
        },
        post: (request, opt) => {
            return useFetch(request, {
                baseURL: config.public.baseURL, ...opt, server: settings.SERVER,
                method: 'POST'
            })
        },
        $post: (request, opt) => {
            return useFetch(request, {
                baseURL: config.public.baseURL, ...opt, server: settings.SERVER,
                method: 'POST',
                onRequest({request, options}) {
                    // Set the request headers
                    options.headers = options.headers || {}
                    options.headers.Authorization = `Token ${getUserToken()}`
                }
            })
        },

    }
}