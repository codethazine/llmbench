<template>
  <div class="h-full p-5">
    <h1 class="text-4xl font-bold mb-4">{{ modelName }}</h1>
    <div class="mb-4 flex flex-wrap space-x-2 justify-center">
      <button @click="setActiveTab('drift')" class="btn btn-primary w-full sm:w-auto">{{ 'Drift' }}</button>
      <button disabled class="btn btn-outline btn-accent w-full sm:w-auto mt-2 sm:mt-0">{{ 'Performance (Coming Soon)' }}</button>
      <button disabled class="btn btn-outline btn-accent w-full sm:w-auto mt-2 sm:mt-0">{{ 'Speed (Coming Soon)' }}</button>
    </div>
    
    <div v-if="activeTab === 'drift'" class="mb-4">
      <div class="flex flex-wrap items-center justify-center space-x-2">
        <label class="input input-bordered w-full sm:w-1/4 mt-2">
          <select v-model="selectedOption" class="w-full bg-transparent text-white rounded focus:outline-none py-3 px-4 mb-3 leading-tight ">
            <option>Solving Math Problems</option>
            <option>Answering Sensitive Questions</option>
            <option>Code Generation</option>
            <option>Visual Reasoning</option>
          </select>
        </label>

        <label class="label w-full sm:w-auto mt-2 ml-0 sm:ml-5">
          <span class="mr-2">From</span>
          <input type="month" class="input input-bordered focus:outline-none" v-model="fromMonth">
        </label>
        <label class="label w-full sm:w-auto mt-2 ml-0 sm:ml-5">
          <span class="mr-2">To</span>
          <input type="month" class="input input-bordered focus:outline-none" v-model="toMonth">
        </label>
      </div> <!-- end flex container -->
      <div class="mt-5 flex flex-col sm:flex-row justify-around items-center">
        <div class="w-full h-full sm:w-1/3 lg:w-1/3 mb-4 sm:mb-0">
            <div>
                <canvas :id="'accChart'+modelId"></canvas>
            </div>
        </div>
        <div class="w-full h-full sm:w-1/3 lg:w-1/3 mb-4 sm:mb-0">
            <div>
                <canvas :id="'verbChart'+modelId"></canvas>
            </div>
        </div>
        <div class="w-full h-full sm:w-1/3 lg:w-1/3 mb-4 sm:mb-0">
            <div>
                <canvas :id="'overlapChart'+modelId"></canvas>
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
// TODO: import model data from Gnosis Chain - faucet currently not working

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
    const accChart = ref(null);
    const verbChart = ref(null);
    const overlapChart = ref(null);

    const setActiveTab = (tabName) => {
      activeTab.value = tabName;
    }

    const getMonthName = (dateString) => {
      const date = new Date(dateString);
      return date.toLocaleString('default', { month: 'long' });
    }

    const chartLabels = computed(() => {
      switch(selectedOption.value) {
        case 'Solving Math Problems':
          return ['Accuracy', 'Verbosity', 'Overlap'];
        case 'Answering Sensitive Questions':
          return ['Answer Rate', 'Verbosity', 'Overlap'];
        case 'Code Generation':
          return ['Directly Executable', 'Verbosity', 'Overlap'];
        case 'Visual Reasoning':
          return ['Exact Match', 'Verbosity', 'Overlap'];
        default:
          return ['Accuracy', 'Verbosity', 'Overlap'];
      }
    });

    let accuracy_from, accuracy_to, verbosity_from, verbosity_to, overlap;
    let answer_rate_from, answer_rate_to, directly_executable_from, directly_executable_to, exact_match_from, exact_match_to;

    const chartData = computed(() => {
      switch(selectedOption.value) {
        case 'Solving Math Problems':
          // Get the data for the selected month
          accuracy_from = modelData.value[fromMonth.value][props.modelId]['mathsolve_accuracy'];
          accuracy_to = modelData.value[toMonth.value][props.modelId]['mathsolve_accuracy'];
          verbosity_from = modelData.value[fromMonth.value][props.modelId]['mathsolve_verbosity'];
          verbosity_to = modelData.value[toMonth.value][props.modelId]['mathsolve_verbosity'];
          overlap = (accuracy_from + accuracy_to) / 2
          console.log(overlap)
          return [accuracy_from, accuracy_to, verbosity_from, verbosity_to, overlap];
        case 'Answering Sensitive Questions':
          answer_rate_from = modelData.value[fromMonth.value][props.modelId]['sensitiveq_answer_rate'];
          answer_rate_to = modelData.value[toMonth.value][props.modelId]['sensitiveq_answer_rate'];
          verbosity_from = modelData.value[fromMonth.value][props.modelId]['sensitiveq_verbosity'];
          verbosity_to = modelData.value[toMonth.value][props.modelId]['sensitiveq_verbosity'];
          overlap = (answer_rate_from + answer_rate_to) / 2
          return [answer_rate_from, answer_rate_to, verbosity_from, verbosity_to, overlap];
        case 'Code Generation':
          directly_executable_from = modelData.value[fromMonth.value][props.modelId]['codegen_directly_executable'];
          directly_executable_to = modelData.value[toMonth.value][props.modelId]['codegen_directly_executable'];
          verbosity_from = modelData.value[fromMonth.value][props.modelId]['codegen_verbosity'];
          verbosity_to = modelData.value[toMonth.value][props.modelId]['codegen_verbosity'];
          overlap = (directly_executable_from + directly_executable_to) / 2
          return [directly_executable_from, directly_executable_to, verbosity_from, verbosity_to, overlap];
        case 'Visual Reasoning':
          exact_match_from = modelData.value[fromMonth.value][props.modelId]['vizreason_exact_match'];
          exact_match_to = modelData.value[toMonth.value][props.modelId]['vizreason_exact_match'];
          verbosity_from = modelData.value[fromMonth.value][props.modelId]['vizreason_verbosity'];
          verbosity_to = modelData.value[toMonth.value][props.modelId]['vizreason_verbosity'];
          overlap = (exact_match_from + exact_match_to) / 2
          return [exact_match_from, exact_match_to, verbosity_from, verbosity_to, overlap];
        default:
          return ['Accuracy', 'Verbosity', 'Overlap'];
      }
    });

    const createAccChart = () => {
      if (accChart.value) {
        accChart.value.destroy();
      }
      
      accChart.value = new Chart(document.getElementById('accChart'+props.modelId), {
        type: 'bar',
        data: {
          labels: [chartLabels.value[0]],
          datasets: [{
            label: getMonthName(fromMonth.value),
            data: [chartData.value[0]], // Update this data depending on your modelData
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }, {
            label: getMonthName(toMonth.value),
            data: [chartData.value[1]], // Update this data depending on your modelData
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

    const createVerbChart = () => {
      if (verbChart.value) {
        verbChart.value.destroy();
      }
      
      verbChart.value = new Chart(document.getElementById('verbChart'+props.modelId), {
        type: 'bar',
        data: {
          labels: [chartLabels.value[1]],
          datasets: [{
            label: getMonthName(fromMonth.value),
            data: [chartData.value[2]], // Update this data depending on your modelData
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }, {
            label: getMonthName(toMonth.value),
            data: [chartData.value[3]], // Update this data depending on your modelData
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

    const createOverlapChart = () => {
      if (overlapChart.value) {
        overlapChart.value.destroy();
      }
      
      overlapChart.value = new Chart(document.getElementById('overlapChart'+props.modelId), {
        type: 'bar',
        data: {
          labels: [chartLabels.value[2]],
          datasets: [{
            label: "overlap rate",
            data: [chartData.value[4]], // Update this data depending on your modelData
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


    onMounted(() => {
      createAccChart();
      createVerbChart();
      createOverlapChart();
    });
    watch([fromMonth, toMonth, selectedOption], () => {
      createAccChart();
      createVerbChart();
      createOverlapChart();
    });


    return {
      activeTab,
      selectedOption,
      fromMonth,
      toMonth,
      setActiveTab,
      accChart,
      verbChart,
      overlapChart
    }
  }
}
</script>
<style scoped>
</style>