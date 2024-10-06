import {defineStore} from "pinia";

export const UserData = defineStore('user', {
    state: () => ({
        token: '',
    }),
    actions: {
        getToken() {
            return this.token
        },
        setToken(name) {
            this.token = token
        }
    },
      persist: true,
})