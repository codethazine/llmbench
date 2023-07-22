<template>
    <div>
      <canvas id="sensitiveQuestionChart"></canvas>
    </div>
  </template>
  
  <script>
  import { onMounted, ref } from 'vue';
  import { Chart, BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
  
  Chart.register(BarController, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
  
  export default {
    name: 'SensitiveQuestionChart',
    props: ['fromMonth', 'toMonth'],
    setup() {
      const chart = ref(null);
      
      onMounted(() => {
        chart.value = new Chart(document.getElementById('sensitiveQuestionChart'), {
          type: 'bar',
          data: {
            labels: ['Answer Rate', 'Verbosity', 'Overlap'],
            datasets: [{
              label: 'March 2023',
              data: [45, 59, 65],
              backgroundColor: 'rgba(153, 102, 255, 0.2)',
              borderColor: 'rgba(153, 102, 255, 1)',
              borderWidth: 1
            }, {
              label: 'June 2023',
              data: [38, 68, 55],
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
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
  