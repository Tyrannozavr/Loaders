import nuxtStorage from 'nuxt-storage';
import {get} from "#ui/utils/index.js";

const settings = {
    SERVER: true
}


export function getUserToken() {
    const tokenString = localStorage.getItem('access_token')
    // console.log(tokenString)
    // console.log('items', localStorage)
    // const token = JSON.parse(tokenString)
    // return token.value
    if (tokenString === null) {
        return ''
    } else {
        const token = JSON.parse(tokenString)
        return token.value
    }

}

export default () => {
    const nuxtApp = useNuxtApp()
    const config = useRuntimeConfig();
    const fetchWithAuth = async (request, method, opt) => {
        opt.body = JSON.stringify(opt.body)
        const response = await fetch(`${config.public.baseURL}${request}`, {
            method: method,
            headers: {
                'Authorization': `Token ${getUserToken()}`,
                'Content-Type': 'application/json', // Optional, depending on your API
                ...opt.headers // Include any additional headers from options
            },
            ...opt
        });

        if (response.status === 401) {
            console.error("Error with login", response.json(), 'token', getUserToken())
            await nuxtApp.runWithContext(() =>
                navigateTo('/login')
            )
        }
        if (!response.ok) {
            console.error(response.json())
        }
        return response;
    }
    return {
        get: async (request, opt = {}) => {
            if (!opt.hasOwnProperty('server')) {
                opt.server = true;
            }
            return fetch(`${config.public.baseURL}${request}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    ...opt.headers
                },
                ...opt
            }).then(response => response.json());
        },
        $get: (request, opt = {}) => {
            return fetchWithAuth(request, 'GET', opt);
        },
        post: async (request, opt) => {
            return fetch(`${config.public.baseURL}${request}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(opt.body), // Ensure body is stringified
            });
        },
        $post: (request, opt = {}) => {
            return fetchWithAuth(request, 'POST', opt);
        },
        put: (request, opt) => {
            return fetchWithAuth(request, 'PUT', opt);
        },
        $put: (request, opt) => {
            return fetchWithAuth(request, 'PUT', opt);
        },
        patch: (request, opt) => {
            return fetchWithAuth(request, 'PATCH', opt);
        },
        $patch: (request, opt) => {
            return fetchWithAuth(request, 'PATCH', opt);
        },
        delete: (request, opt) => {
            return fetchWithAuth(request, 'DELETE', opt);
        },
        $delete: (request, opt = {}) => {
            return fetchWithAuth(request, 'DELETE', opt);
        },
    }
}
