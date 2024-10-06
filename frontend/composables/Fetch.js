import nuxtStorage from 'nuxt-storage';

const settings = {
    SERVER: true
}

export function getUserToken() {
    const tokenString = localStorage.getItem('access_token')
    const token = JSON.parse(tokenString)
    return token.value
}

export default () => {
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

        if (!response.ok) {
            console.error(response.json())
            // throw new Error(HTTP error! status: ${response.status});
        }
        return response; // Parse JSON response
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
        $get: (request, opt) => {
            return fetchWithAuth(request, 'GET', opt);
        },
        post: async (request, opt) => {
            return fetch(`${config.public.baseURL}${request}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(opt.body), // Ensure body is stringified
            }).then(response => response.json());
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
        $delete: (request, opt) => {
            return fetchWithAuth(request, 'DELETE', opt);
        },
    }
}
