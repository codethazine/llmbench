<template>
  <div class="h-full p-5">
    <h1 class="text-4xl font-bold mb-4">{{ modelName }}</h1>
    <div class="mb-4">
      <button @click="setActiveTab('drift')" class="btn btn-primary mr-2">{{ 'Drift' }}</button>
      <button disabled class="btn btn-outline btn-accent">{{ 'Performance (Coming Soon)' }}</button>
      <button disabled class="btn btn-outline btn-accent ml-2">{{ 'Speed (Coming Soon)' }}</button>
    </div>
    
    <div v-if="activeTab === 'drift'" class="mb-4">
      <div class="flex items-center justify-center">
        <label class="input input-bordered w-1/4">
          <select v-model="selectedOption" class="w-full bg-transparent text-white rounded focus:outline-none py-3 px-4 mb-3 leading-tight ">
            <option>Solving Math Problems</option>
            <option>Answering Sensitive Questions</option>
            <option>Code Generation</option>
            <option>Visual Reasoning</option>
          </select>
        </label>

        <label class="label ml-5">
          <span class="mr-2">From</span>
          <input type="month" class="input input-bordered focus:outline-none" v-model="fromMonth">
        </label>
        <label class="label ml-5">
          <span class="mr-2">To</span>
          <input type="month" class="input input-bordered focus:outline-none" v-model="toMonth">
        </label>
      </div> <!-- end flex container -->
      <div class="mt-5 flex flex-col items-center">
        <div class="w-full h-full sm:w-3/4 sm:h-3/4 lg:w-1/2 lg:h-1/2">
          <div>
            <canvas id="benchmarkChart"></canvas>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, toRefs, watch, computed } from 'vue'
import { Chart, BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

import importedModelData from '@/assets/total_hist_eval.json'

Chart.register(BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default {
  name: 'ModelBenchmark',
  props: ['modelName', 'modelId'],
  setup(props) {
    const modelData = ref(importedModelData);

    const activeTab = ref('drift');
    const selectedOption = ref('Solving Math Problems');
    const fromMonth = ref('2023-03');
    const toMonth = ref('2023-06');
    const chart = ref(null);

    console.log(modelData.value)
    console.log(props.modelName)
    console.log(props.modelId)


    const setActiveTab = (tabName) => {
      activeTab.value = tabName;
    }

    const getMonthName = (dateString) => {
      const date = new Date(dateString);
      return date.toLocaleString('default', { month: 'long' });
    }
    const createChart = () => {
      if (chart.value) {
        chart.value.destroy();
      }
      
      chart.value = new Chart(document.getElementById('benchmarkChart'), {
        type: 'bar',
        data: {
          labels: ['Accuracy', 'Verbosity', 'Overlap'],
          datasets: [{
            label: getMonthName(fromMonth.value),
            data: [65, 59, 80], // Update this data depending on your modelData
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }, {
            label: getMonthName(toMonth.value),
            data: [28, 48, 40], // Update this data depending on your modelData
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    };

    onMounted(createChart);
    watch([fromMonth, toMonth, selectedOption], createChart); // Recreate the chart when fromMonth, toMonth, or selectedOption changes

    return {
      activeTab,
      selectedOption,
      fromMonth,
      toMonth,
      setActiveTab,
      chart
    }
  }
}
</script>
