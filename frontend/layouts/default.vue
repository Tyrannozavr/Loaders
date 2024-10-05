<template>
  <div class="layout bg-white p-1">
    <div class="max-w-screen-2xl">
      <Header class="rounded-lg"/>
      <div class="content">
        <Sidebar class="bg-stone-300"/>
        <main class="main-content rounded-lg bg-stone-300 text-black">
          <NuxtPage/>
        </main>
      </div>
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
  max-width: 1580px;
}

.main-content {
  flex-grow: 1; /* Занимает оставшееся пространство */
  padding: 5px 10px 5px 10px; /* Отступы для основного контента */
  //background: #ccc;
}

</style>
