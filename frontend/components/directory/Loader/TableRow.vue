<script setup lang="ts">
import formatDate from "~/utils/FormatData";

const $backend = Fetch()
const props = defineProps({
  loader: {
    required: true,
    type: Object
  },
})
const localLoader = ref(props.loader)
const emits = defineEmits(['refresh'])


const actions = ref([{
  label: 'Не сохранять',
  click: () => {
    alert('not edited')
    underEdition.value = false
    localLoader.value = props.loader

  }
}, {
  label: 'Вернуться к редактированию',
}])

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
const saveRow = async () => {
  underEdition.value = false
  if (props.loader.creation) {
    try {
      const response = await $backend.$post(`loaders/`, {
        body: {
          brand: localLoader.value.brand,
          number: localLoader.value.number,
          capacity: localLoader.value.capacity
        }
      })
      if (response.status === 201) {
        toast.add({title: "Отправлено успешно"})
        emits('refresh')
      }
    } catch (error) {
      console.error('Ошибка:', error);
    }
  } else {
    // row edition
    if ((!localLoader.value.brand) || (!localLoader.value.number) || (!localLoader.value.capacity)) {
      toast.add({title: "Заполните все поля!"})
    } else {
      console.log(localLoader.value)
      console.log(localLoader.value.id)
      try {
        const response = await $backend.$put(`loaders/${localLoader.value.id}/`, {
          body: {
            brand: localLoader.value.brand,
            number: localLoader.value.number,
            capacity: localLoader.value.capacity
          }
        })
        if (response.status === 200) {
          toast.add({title: "Изменено успешно"})
          emits('refresh')
        }
      } catch (error) {
        console.error('Ошибка:', error);
      }
    }
  }
}
const deleteRow = async () => {
  if (!props.loader.creation) {
    if (!underEdition.value) {
      try {
        const response = await $backend.$delete(`loaders/${localLoader.value.id}/`)
        if (response.status === 204) {
          toast.add({title: "Успешно удалено"})
        } else {
          if (response.status === 400)
          toast.add({title: "Если для погрузчика имеются зарегистрированные простои – удаление запрещено"})
        }
      } catch (error) {
        console.error(error)
      }
      underEdition.value = false
    } else {
      // console.log('cancel edition')
      toast.add({title: "Не сохранять внесенные изменения? Вы уверены?", actions})
    }
  } else {
    console.log('cancel creation')
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
      <td>
        <UInput v-model="localLoader.brand"/>
      </td>
      <td>
        <UInput v-model="localLoader.number"/>
      </td>
      <td>
        <UInput type="number" v-model="localLoader.capacity"/>
      </td>
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
      <DirectoryEditIcons
          :is-under-edition="underEdition"
          @cancel="deleteRow"
          @edit="editRow"
          @save="saveRow"
      />
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