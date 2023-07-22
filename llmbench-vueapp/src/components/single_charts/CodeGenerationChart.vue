<template>
    <div>
      <canvas id="codeGenerationChart"></canvas>
    </div>
  </template>
  
  <script>
  import { onMounted, ref } from 'vue';
  import { Chart, BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
  
  Chart.register(BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
  
  export default {
    name: 'CodeGenerationChart',
    props: ['fromMonth', 'toMonth', 'modelData'],
    setup() {
      const chart = ref(null);
      
      onMounted(() => {
        chart.value = new Chart(document.getElementById('codeGenerationChart'), {
          type: 'bar',
          data: {
            labels: ['Directly Executable', 'Verbosity', 'Overlap'],
            datasets: [{
              label: 'March 2023',
              data: [35, 79, 70],
              backgroundColor: 'rgba(255, 206, 86, 0.2)',
              borderColor: 'rgba(255, 206, 86, 1)',
              borderWidth: 1
            }, {
              label: 'June 2023',
              data: [48, 58, 60],
              backgroundColor: 'rgba(54, 162, 235, 0.2)',
              borderColor: 'rgba(54, 162, 235, 1)',
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
      });
  
      return { chart };
    }
  }
  </script>
  