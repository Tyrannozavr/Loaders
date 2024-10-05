<script setup lang="ts">
const props = defineProps({
  loader: {
    required: true,
    type: Object
  },
})
const emits = defineEmits(['refresh'])
const formatDate = (datetime) => {
  if (!datetime) {
    return ''
  }
  const date = new Date(datetime);
  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0'); // Months are zero-based
  const year = date.getFullYear();
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');

  return `${day}.${month}.${year} ${hours}:${minutes}`;
}
const underEdition = ref(false)
if (props.loader.creation) {
  underEdition.value = true
}
const User = ref()
User.value = {"fio": "dmitry"}
const toast = useToast()
const editRow = () => {
  if (!User.value) {
    toast.add({title: "Войдите в систему чтобы вносить изменения"})
  } else {
    underEdition.value = true
  }
}
const saveRow = () => {
  underEdition.value = false
}
const deleteRow = () => {
  if (!props.loader.creation) {
    console.log('delete row')
  }
  emits('refresh')
}
</script>

<template>
  <tr style="height:10px" :key="loader.id">
    <td>{{ loader.id }}</td>
    <slot v-if="(!underEdition)">
      <td>{{ loader.brand }}</td>
      <td>{{ loader.number }}</td>
      <td>{{ loader.capacity }}</td>
    </slot>
    <slot v-else>
      <td><UInput v-model="loader.brand"/></td>
      <td><UInput v-model="loader.number"/></td>
      <td><UInput type="number" v-model="loader.capacity"/></td>
    </slot>

    <td>
      <div class="is_active rounded-xl" v-if="loader.id">
        <UIcon name="mi:check" v-if="loader.isActive" class=" text-green-700"/>
        <UIcon name="mi:close" class=" text-red-700" v-else/>
      </div>
      <div v-else></div>
    </td>
    <td>{{ formatDate(loader.datetime) }}</td>
    <td>{{ loader.user }}</td>
    <td class="edit_cell">
      <div class="edit_container">
        <button>
          <UIcon name="rivet-icons:pencil-solid" class="text-gray-500 w-5 h-5"
                 v-if="(!underEdition)" @click="editRow" />
          <UIcon name="rivet-icons:check" class="text-gray-500 w-5 h-5"
                 v-else @click="saveRow"/>
        </button>
        <button @click="deleteRow">
          <UIcon name="rivet-icons:close" class="text-gray-500 w-5 h-5"/>
        </button>
      </div>

    </td>
  </tr>
</template>

<style scoped>

.is_active {
  border-width: 1px; /* Ensure border width is 1px */
  width: 80%;
  height: 100%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  vertical-align: middle;
}

.edit_container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 5px;
}

th, td {
  border-right: 1px solid #ccc; /* Right border for each cell */
  border-bottom: 1px solid #ccc;
  padding: 0 4px; /* Add some padding for better spacing */
  text-align: center;
}

tr {
  height: 10px;
}

</style>