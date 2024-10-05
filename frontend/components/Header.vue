<template>
  <header class="header min-h-20 bg-red-700">
    <div class="container">
      <nav>
        <UButton class="profile h-10 rounded-2xl font-bold w-36"
                 color="black"
                 variant="solid">Профиль</UButton>
<!--        <UButton class="profile" size="lg" color="black" variant="solid">Профиль</UButton>-->
      </nav>
    </div>
  </header>
</template>

<script setup>
import {ref} from 'vue';
import {useRouter} from 'vue-router';

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
  color: white;
  padding: 10px 20px;
  margin: 2px 0 15px 0;
  justify-content: center;
}

.container {
  display: flex;
  width: 100%;
}

nav {
  width: 100%;
  display: flex;
  align-items: center;
  padding-top: 15px;
}

.profile {
  margin-left: auto;
  justify-content: center;
}
</style>
