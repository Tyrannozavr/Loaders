<template>
  <div>
    <h1>Справочник Погрузчики</h1>

    <input v-model="searchQuery" placeholder="Номер погрузчика" />
    <button @click="searchLoaders">Искать</button>
    <button @click="resetFilter">Сбросить фильтр</button>
    <button @click="openLoaderForm">Добавить</button>

    <LoaderTable
      :loaders="filteredLoaders"
      @edit="openLoaderForm"
      @delete="confirmDeleteLoader"
    />

    <IncidentTable
      v-if="selectedLoader"
      :incidents="selectedLoader.incidents"
      @add="openIncidentForm"
      @edit="openIncidentForm"
      @delete="confirmDeleteIncident"
    />

    <LoaderForm
      v-if="isLoaderFormVisible"
      :loader="currentLoader"
      @close="closeLoaderForm"
      @save="saveLoader"
    />

    <IncidentForm
      v-if="isIncidentFormVisible"
      :incident="currentIncident"
      @close="closeIncidentForm"
      @save="saveIncident"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import LoaderTable from '~/components/directory/Loader/Table.vue';
import LoaderForm from '~/components/directory/LoaderForm.vue';
import IncidentTable from '~/components/directory/IncidentTable.vue';
import IncidentForm from '~/components/directory/IncidentForm.vue';

const loaders = ref([]);
const searchQuery = ref('');
const filteredLoaders = ref(loaders.value);
const isLoaderFormVisible = ref(false);
const isIncidentFormVisible = ref(false);
const currentLoader = ref(null);
const currentIncident = ref(null);
const selectedLoader = ref(null);

const searchLoaders = () => {
  filteredLoaders.value = loaders.value.filter(loader =>
    loader.number.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
};

const resetFilter = () => {
  searchQuery.value = '';
  filteredLoaders.value = loaders.value;
};

const openLoaderForm = (loader) => {
  currentLoader.value = loader || {};
  isLoaderFormVisible.value = true;
};

const closeLoaderForm = () => {
  isLoaderFormVisible.value = false;
};

const saveLoader = (loader) => {
  // Сохранение логики
};

const confirmDeleteLoader = (loader) => {
  // Логика подтверждения удаления
};

const openIncidentForm = (incident) => {
  currentIncident.value = incident || {};
  isIncidentFormVisible.value = true;
};

const closeIncidentForm = () => {
  isIncidentFormVisible.value = false;
};

const saveIncident = (incident) => {
  // Сохранение инцидента
};

const confirmDeleteIncident = (incident) => {
  // Логика подтверждения удаления инцидента
};
</script>
