<template>
  <div class="h-full p-5">
    <h1 class="text-4xl font-bold mb-4">{{ modelName }}</h1>
    <div class="mb-4">
      <button @click="setActiveTab('drift')" class="btn btn-primary mr-2">{{ 'Drift' }}</button>
      <button disabled class="btn btn-outline btn-accent">{{ 'Performance (Coming Soon)' }}</button>
      <button disabled class="btn btn-outline btn-accent ml-2">{{ 'Speed (Coming Soon)' }}</button>
    </div>
    
    <div v-if="activeTab === 'drift'" class="mb-4">
      <label class="input input-bordered w-1/4">
        <select v-model="selectedOption">
          <option>Solving Math Problems</option>
          <option>Answering Sensitive Questions</option>
          <option>Code Generation</option>
          <option>Visual Reasoning</option>
        </select>
      </label>

      <div class="flex items-center">
        <label class="label ml-5">
          <span>From</span>
          <input type="month" class="input input-bordered" v-model="fromMonth">
        </label>
        <label class="label ml-5">
          <span>To</span>
          <input type="month" class="input input-bordered" v-model="toMonth">
        </label>
      </div>

      <div class="mt-5 flex flex-col items-center">
        <div class="w-full h-full sm:w-3/4 sm:h-3/4 lg:w-1/2 lg:h-1/2">
          <component :is="chartComponent" :from-month="fromMonth" :to-month="toMonth" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import MathProblemChart from './MathProblemChart'
import SensitiveQuestionChart from './SensitiveQuestionChart'
import CodeGenerationChart from './CodeGenerationChart'
import VisualReasoningChart from './VisualReasoningChart'

export default {
  name: 'ModelBenchmark',
  props: ['modelName'],
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
