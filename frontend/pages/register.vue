<template>
  <div class="flex items-center justify-center min-h-screen">
    <form @submit.prevent="register" class="bg-white p-6 rounded shadow-md w-96">
      <h2 class="text-lg font-bold mb-4">Register</h2>
      <input v-model="firstName" type="text" placeholder="Имя" class="input-field" required/>
      <input v-model="surname" type="text" placeholder="Отчество" class="input-field" required/>
      <input v-model="lastName" type="text" placeholder="Фамилия" class="input-field" required/>
      <input v-model="email" type="email" placeholder="Email" class="input-field" required/>
      <input v-model="password" type="password" placeholder="Пароль" class="input-field" required/>
      <input v-model="repeatPassword" type="password" placeholder="Повторите пароль" class="input-field" required/>
      <p v-if="passwordMismatch" class="text-red-500">Passwords do not match.</p>
      <button type="submit" class="btn :disabled='passwordMismatch'">Зарегистрироваться</button>
      <p class="mt-4">
        Уже есть аккаунт?
        <nuxt-link to="/login" class="text-blue-500">войти</nuxt-link>
        .
      </p>
    </form>
  </div>
</template>

<script setup>
const firstName = ref('');
const surname = ref('');
const lastName = ref('');
const email = ref('');
const password = ref('');
const repeatPassword = ref('');

const passwordMismatch = computed(() => password.value !== repeatPassword.value);

const register = async () => {
  if (passwordMismatch.value) return; // Prevent submission if passwords do not match

  try {
    const response = await $fetch('http://localhost:3000/register', {
      method: 'POST',
      body: {
        first_name: firstName.value,
        surname: surname.value,
        last_name: lastName.value,
        email: email.value,
        password: password.value,
      },
    });
    // Handle success response
    console.log(response);
  } catch (error) {
    console.error('Ошибка регистрации:', error);
  }
};
</script>

<style>
.input-field {
  @apply w-full p-2 border rounded mb-4;
}

.btn {
  @apply w-full bg-red-700 text-white p-2 rounded;
}
</style>
