<template>
  <div class="layout bg-white p-1" >
    <Header class="rounded-lg" />
    <div class="content">
      <Sidebar class="bg-stone-300" />
      <main class="main-content rounded-lg bg-stone-300">
        <NuxtPage />
      </main>

    </div>
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue';
import Sidebar from '@/components/Sidebar.vue';
</script>

<style scoped>
.layout {
  display: flex;
  flex-direction: column; /* Заголовок в столбик */
  height: 100vh; /* Полная высота экрана */
}

.content {
  display: flex;
  flex-grow: 1; /* Основной контент занимает оставшееся пространство */
}

.main-content {
  flex-grow: 1; /* Занимает оставшееся пространство */
  padding: 20px; /* Отступы для основного контента */
  //background: #ccc;
}


body {
  background-color: white; /* Белый фон для всего сайта */
}
</style>
