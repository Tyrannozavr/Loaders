<script setup lang="ts">
const $backend = Fetch()

const search = () => {
  // const response = $backend.$post('loaders/')
  // console.log(response, typeof response)
}
</script>

<template>
  <div class="search_container">
    <div class="search_name">Номер погрузчика</div>
    <div class="search_field">
      <input
          type="text"
          class="rounded-3xl w-28 bg-white h-7"
      /></div>
    <UButton
        class="bg-red-700 search_button"
        icon="weui:search-filled"
        size="sm"
        color="primary"
        variant="solid"
        label="Искать"
        :trailing="false"
        @click="search"
    />
    <div class="search_reset">
      <UIcon
          name="mi:close"
          class="text-red-700"
      />
      Сбросить фильтр
    </div>
  </div>
</template>

<style scoped>
.search_container {
  display: flex;
  flex-direction: row;
  gap: 15px;
  margin-bottom: 40px;
}

.search_button {
  width: 120px;
  justify-content: center;
}

.search_reset {
  display: flex; /* Use flexbox */
  align-items: center; /* Center items vertically */
  cursor: pointer;
}
</style>