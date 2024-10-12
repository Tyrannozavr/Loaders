import type { JWTPayload } from "@/types/auth";

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: '',
    refreshToken: '',
  }),
  getters: {
    getTokenData(state: any): JWTPayload | null {
      if (!state.accessToken) return null;

      try {
        const tokenParts = state.accessToken.split('.');
        if (tokenParts.length !== 3) {
          throw new Error(`Access token decode error. Need 3 parts, got ${tokenParts.length}`);
        }

        const { $decodeBase64 } = useNuxtApp()
        const payload = JSON.parse($decodeBase64(tokenParts[1])) as JWTPayload;
        return payload;
      } catch (e: any) {
        console.error('Failed to parse JWT token:', e);
        return null;
      }
    },
  },
  persist: true,
  actions: {
    setTokens(accessToken: string, refreshToken: string) {
      this.accessToken = accessToken;
      this.refreshToken = refreshToken;
    },
    clearTokens() {
      this.accessToken = '';
      this.refreshToken = '';
    },
  },
})
