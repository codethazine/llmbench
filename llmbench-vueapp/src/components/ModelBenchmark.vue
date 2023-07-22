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
          <component :is="chartComponent" :from-month="fromMonth" :to-month="toMonth" :model-data="modelData" :model-id="modelId"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import MathProblemChart from './single_charts/MathProblemChart'
import SensitiveQuestionChart from './single_charts/SensitiveQuestionChart'
import CodeGenerationChart from './single_charts/CodeGenerationChart'
import VisualReasoningChart from './single_charts/VisualReasoningChart'

import modelData from '@/assets/total_hist_eval.json'

export default {
  name: 'ModelBenchmark',
  props: ['modelName', 'modelId'],
  data() {
    return {
      modelData: {}
    }
  },
  mounted() {
    // Assign the imported JSON data to the component's jsonData
    this.modelData = modelData;
  },
  setup() {
    const activeTab = ref('drift');
    const selectedOption = ref('Solving Math Problems');
    const fromMonth = ref('2023-03');
    const toMonth = ref('2023-06');
    
    const setActiveTab = (tabName) => {
      activeTab.value = tabName;
    }

    const chartComponent = computed(() => {
      switch (selectedOption.value) {
        case 'Solving Math Problems':
          return MathProblemChart;
        case 'Answering Sensitive Questions':
          return SensitiveQuestionChart;
        case 'Code Generation':
          return CodeGenerationChart;
        case 'Visual Reasoning':
          return VisualReasoningChart;
        default:
          return null;
      }
    })

    return {
      activeTab,
      selectedOption,
      fromMonth,
      toMonth,
      setActiveTab,
      chartComponent
    }
  }
}
</script>
