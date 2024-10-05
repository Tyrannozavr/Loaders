<template>
  <header class="header">
    <div class="container">
      <h1>Справочник Погрузчиков</h1>
      <nav>
        <ul>
          <li v-if="!isLoggedIn">
            <button @click="goToLogin">Вход</button>
            <button @click="goToRegister">Регистрация</button>
          </li>
          <li v-else>
            <button @click="goToProfile">Профиль</button>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const isLoggedIn = ref(false); // Замените это значение на актуальное состояние входа пользователя
const router = useRouter();

const goToLogin = () => {
  router.push('/login'); // Путь к странице входа
};

const goToRegister = () => {
  router.push('/register'); // Путь к странице регистрации
};

const goToProfile = () => {
  router.push('/profile'); // Путь к странице профиля
};
</script>

<style scoped>
.header {
  background-color: red;
  color: white;
  padding: 10px 20px;
  margin: 2px 0 15px 0;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav ul {
  list-style-type: none;
  display: flex;
  gap: 15px;
}

nav button {
  background: transparent;
  border: none;
  color: white;
  cursor: pointer;
}
</style>
