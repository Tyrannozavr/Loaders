<template>
  <div class="modal">
    <h2>{{ loader.id ? 'Редактировать' : 'Добавить' }} Погрузчик</h2>
    <input v-model="loader.brand" placeholder="Марка погрузчика" />
    <input v-model="loader.number" placeholder="Номер погрузчика" />
    <input type="number" v-model="loader.capacity" placeholder="Грузоподъемность" step="0.001" />

    <button @click="save">Сохранить</button>
    <button @click="$emit('close')">Отмена</button>
  </div>
</template>

<script setup>
defineProps(['loader']);
const emit = defineEmits(['close', 'save']);

const save = () => {
  emit('save', loader);
};
</script>
