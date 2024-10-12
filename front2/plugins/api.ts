import type { SignInResponse } from '@/types/auth'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig();
  const authStore = useAuthStore();

  const api = $fetch.create({
    baseURL: config.public.apiBaseURL,
    onRequest({ options }) {
      const accessToken = authStore.accessToken;
      if (accessToken) {
        const headers = options.headers ||= {}
        if (Array.isArray(headers)) {
          headers.push(['Authorization', `Bearer ${accessToken}`])
        } else if (headers instanceof Headers) {
          headers.set('Authorization', `Bearer ${accessToken}`)
        } else {
          headers.Authorization = `Bearer ${accessToken}`
        }
      }
    },
    async onResponseError({ request, response, options }) {
      if (response.status === 401 && (request as any).url !== '/auth/refresh') {
        try {
          const refreshToken = authStore.refreshToken
          const refreshResponse = await $fetch<SignInResponse>('/auth/refresh', {
            method: 'POST',
            baseURL: config.public.apiBaseURL,
            body: { refreshToken: refreshToken },
          });
          authStore.setTokens(refreshResponse.accessToken, refreshResponse.refreshToken);

          const accessToken = refreshResponse.accessToken;
          if (accessToken) {
            const headers = options.headers || {}
            if (Array.isArray(headers)) {
              headers.push(['Authorization', `Bearer ${accessToken}`])
            } else if (headers instanceof Headers) {
              headers.set('Authorization', `Bearer ${accessToken}`)
            } else {
              headers.Authorization = `Bearer ${accessToken}`
            }
          } else {
            authStore.clearTokens();
            await navigateTo('/');
          }

          return $fetch(request, options);
        } catch (e) {
          authStore.clearTokens();
          await navigateTo('/');
          return Promise.reject(e);
        }
      }
      return Promise.reject(response);
    },
  });

  return {
    provide: {
      api
    }
  }
});