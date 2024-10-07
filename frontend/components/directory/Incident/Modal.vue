<script setup>
import {format} from "date-fns";

const props = defineProps({
  modelValue: {
    type: Object,
    default: null
  },
  isActive: {
    type: Boolean,
    default: false
  }
});
const isActive = computed({
  get: () => props.isActive,
  set: (value) => {
    emit('close')
  }
})
const emit = defineEmits(['update:model-value', 'close', 'save']);
const saveModal = () => {
  emit('save')
}
</script>

<template>
<!--  model value is {{modelValue}}-->
  <UModal v-model="isActive">
    <div class="p-4 bg-gray-200 rounded-2xl text-gray-500 font-semibold">
      <div class="modal_header text-center">
        Проблемы с погрузчиком? Опишите
      </div>
      <div class="modal_divider bg-red-700 h-0.5 w-full my-2 mb-3"></div>

      <div class="modal_date_container flex flex-row mb-4">
        <div class="modal_date_start">
          <UPopover :popper="{ placement: 'bottom-start' }">
            Начало
            <UButton :label="format(props.modelValue.dateStart, 'dd.MM.yyyy HH:mm')"
                     class="ml-4 mr-4 bg-white text-black"/>
            <template #panel="{ close }">
              <DatePicker v-model="props.modelValue.dateStart" is-required @close="close"/>
            </template>
          </UPopover>
        </div>
        <div class="modal_date_end">
          <UPopover :popper="{ placement: 'bottom-start' }">
            Окончание
            <UButton v-if="props.modelValue.dateEnd" :label="format(props.modelValue.dateEnd, 'dd.MM.yyyy HH:mm')"
                     class="ml-4 mr-4 bg-white text-black"/>
            <UButton v-else label="еще активен" class="ml-4 mr-4 bg-white text-black"/>
            <template #panel="{ close }">
              <DatePicker v-model="props.modelValue.dateEnd" nullable @close="close"/>
            </template>
          </UPopover>
        </div>
      </div>
      <div class="content mb-4 flex flex-col gap-2">
        описание инцидента
        <textarea cols="50" rows="5" class="rounded-xl" v-model="props.modelValue.description"></textarea>
      </div>
      <div class="modal_buttons flex justify-center gap-10">
        <UButton
            class="w-32 flex justify-center items-center bg-red-700"
            label="Сохранить"
            @click="saveModal"
        />

        <UButton
            class="w-32 flex justify-center items-center bg-gray-500 text-black"
            label="Выход"
            @click="emit('close')"
        />
      </div>
    </div>
  </UModal>
</template>

<style scoped>

</style>
