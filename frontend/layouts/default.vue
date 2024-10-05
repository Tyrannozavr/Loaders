<template>
  <div class="layout p-1 bg-white">
    <div class="layout_container">
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
  gap: 20px;
}

.main-content {
  flex-grow: 1; /* Занимает оставшееся пространство */
  padding: 5px 10px 5px 10px; /* Отступы для основного контента */
}
.layout_container {
  max-width: 1600px;
}
</style>
