<script setup lang="ts">
import formatDate from "~/utils/FormatData";

const props = defineProps(['incident'])
const downTime = computed(() => {
  if (!props.incident.startDate instanceof Date) {
    return ''
  }

  let startDate = new Date(props.incident.startDate);
  let endDate = props.incident.endDate ? new Date(props.incident.endDate) : new Date();
  if (!startDate) {
    return ''
  }

  // Calculate years, months, days, hours, and minutes
  let years = endDate.getFullYear() - startDate.getFullYear();
  let months = endDate.getMonth() - startDate.getMonth();
  let days = endDate.getDate() - startDate.getDate();
  let hours = endDate.getHours() - startDate.getHours();
  let minutes = endDate.getMinutes() - startDate.getMinutes();

  // Adjust for negative values
  if (minutes < 0) {
    minutes += 60;
    hours--;
  }

  if (hours < 0) {
    hours += 24;
    days--;
  }

  if (days < 0) {
    const lastMonth = new Date(endDate.getFullYear(), endDate.getMonth(), 0);
    days += lastMonth.getDate(); // Get the number of days in the previous month
    months--;
  }

  if (months < 0) {
    months += 12;
    years--;
  }

  // Build the result string
  let result = '';

  if (years > 0) {
    result += `${years} лет `;
  }

  if (months > 0) {
    result += `${months} месяцев `;
  }

  if (days > 0) {
    result += `${days} дней `;
  }

  result += `${hours} часов ${minutes} минут`;

  return result.trim(); // Remove any trailing whitespace
});

const isUnderEdition = ref(false)
</script>

<template>
  <tr :key="incident.id">
    <td>{{ formatDate(incident.startDate) }}</td>
    <td>{{ formatDate(incident.endDate) }}</td>
    <td>{{ downTime }}</td>
    <td>{{ incident.description }}</td>

    <td>
      <DirectoryEditIcons
          :is-under-edition="isUnderEdition"
          @cancel="deleteRow"
          @edit="editRow"
          @save="saveRow"
      />
    </td>
  </tr>
</template>

<style scoped>
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