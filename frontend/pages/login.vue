<script setup>
import {ref} from 'vue';
import nuxtStorage from 'nuxt-storage';

const $backend = Fetch()

const email = ref('');
const password = ref('');
const router = useRouter()
const login = async () => {
  try {
    const response = await $backend.post('users/login/', {
      body: {
        email: email.value,
        password: password.value
      }
    })
    nuxtStorage.localStorage.setData('access_token', response.token)
    await router.push('/directory/loaders')

  } catch (error) {
    console.error('Ошибка регистрации:', error);
  }
};
</script>

<template>
  <div class="flex items-center justify-center min-h-screen">
    <form @submit.prevent="login" class="bg-white p-6 rounded shadow-md w-96">
      <h2 class="text-lg font-bold mb-4">Login</h2>
      <input v-model="email" type="email" placeholder="Email" class="input-field" required/>
      <input v-model="password" type="password" placeholder="Пароль" class="input-field" required/>
      <button type="submit" class="btn">Login</button>
      <p class="mt-4">
        Еще нет аккаунта?
        <nuxt-link to="/register" class="text-blue-500">зарегистрироваться</nuxt-link>
        .
      </p>
    </form>
  </div>
</template>


<style>
.input-field {
  @apply w-full p-2 border rounded mb-4;
}

.btn {
  @apply w-full bg-red-700 text-white p-2 rounded;
}
</style>
