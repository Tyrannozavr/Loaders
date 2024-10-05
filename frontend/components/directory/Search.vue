<script setup lang="ts">

</script>

<template>
  <div class="search_container">
    <div class="search_name">Номер погрузчика</div>
    <div class="search_field">
      <input
          type="text"
          class="rounded-3xl w-24 bg-white"
      /></div>
    <div class="search_button">
      <UButton
          class="bg-red-700"
      >Искать
      </UButton>
    </div>
    <div class="search_reset">Сбросить</div>
  </div>
</template>

<style scoped>
.search_container {
  display: flex;
  flex-direction: row;
  gap: 15px;
}
</style>