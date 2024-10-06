<script setup lang="ts">
defineProps(['loaderId'])
const loader = ref({
  number: 1,
  incidentList: [
    {
      id: 1,
      startDate: new Date(),
      endDate: new Date(),
      description: 'description'
    },
    {
      id: 2,
      startDate: new Date(2010, 0, 1, 0, 0, 0, 0),
      endDate: new Date,
      description: 'description'
    },

  ]
})
import {format} from 'date-fns'

const isModalActive = ref(false)
const addRow = () => {
  isModalActive.value = true
  // loader.value.incidentList.push({creation: true})
}
const dateStart = ref(new Date())
const dateEnd = ref(null)
</script>

<template>
  <slot v-if="loaderId">
    <div class="incident_containe">
      <h3 class="incident_header font-bold">Простои по погрузчику {{ loader.number }}</h3>
      <UButton
          class="add_button bg-red-700 w-32 rounded-xl flex items-center justify-center mb-4"
          size="md"
          @click="addRow"
      >Добавить
      </UButton>
      <DirectoryIncidentTable :incidents="loader.incidentList"/>
      <UModal v-model="isModalActive">
        <div class="p-4 bg-gray-200 rounded-2xl text-gray-700 font-semibold">
          <div class="modal_header text-center">
            Проблемы с погрузчиком? Опишите
          </div>
          <UDivider/>
          <div class="modal_date_container flex flex-row">
            <div class="modal_date_start">
              <UPopover :popper="{ placement: 'bottom-start' }">
                Начало
                <UButton :label="format(dateStart, 'dd.MM.yyyy HH:MM')" class="ml-4 mr-4 bg-red-700"/>
                <template #panel="{ close }">
                  <DatePicker v-model="dateStart" is-required @close="close"/>
                </template>
              </UPopover>
            </div>
            <div class="modal_date_end">
              <UPopover :popper="{ placement: 'bottom-start' }">
                Окончание
                <UButton v-if="dateEnd" :label="format(dateEnd, 'dd.MM.yyyy HH:MM')" class="ml-4 mr-4 bg-red-700"/>
                <UButton v-else label="еще активен" class="ml-4 mr-4 bg-red-700"/>
                <template #panel="{ close }">
                  <DatePicker v-model="dateEnd" is-required @close="close"/>
                </template>
              </UPopover>
            </div>
          </div>
        </div>
      </UModal>
    </div>
  </slot>
  <slot v-else></slot>
</template>

<style scoped>
.incident_header {
  margin-bottom: 5px;
}
</style>